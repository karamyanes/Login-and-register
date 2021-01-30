import uuid  #UUID, Universal Unique Identifier, is a python library which helps in generating rando
#objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.). Advantages of UUID
#Useful in generating random documents, addresses etc
#UUIDs are generally used for identifying information that needs to be unique within a system or network thereof
#Their uniqueness and low probability in being repeated makes them useful for being associative keys in databases and identifiers for physical hardware within an organization.
from rest_framework import generics, permissions, views, status
#Permissions are used to grant or deny access for different classes of users to different parts of the API.
#The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.
#STAT: REST framework includes a set of named constants that you can use to make your code more obvious and readable.
from rest_framework.response import Response # we can send back a specific response 
from .serializer import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer #The serializer class that should be used for validating and deserializing input, and for serializing output.

    def post(self, request, *args,  **kwargs):# check Mixins in google
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)# is checking and validating all data sent in request 
        user = serializer.save() #saving all data (after validation) in database 
        return Response({ #return after successful save
            "user": UserSerializer(user, context=self.get_serializer_context()).data,#"user" : return all user data that he entered in the request, enter in the registration
            "message": "User Created Successfully.  Now go to Login to get your token",# custom message between you and the mobile developer
        })


class UserLogoutAll(views.APIView):
    """
    This endpoint to log out all sessions for a given user
    """

    permission_classes = [permissions.IsAuthenticated]# Is user already authenticated (logged in) or not.

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4() #uuid4() Generate a random UUID.
        user.save()

        return Response({
            "status": status.HTTP_204_NO_CONTENT ,
            "message": "User Logged Out"
        })


class CustomTokenObtainPairView(TokenObtainPairView):# we use it to get refresh and access to customize and add extra data username and id by help from TokenObtainPairSerializer
    serializer_class = CustomTokenObtainPairSerializer  #The serializer class that should be used for validating and deserializing input, and for serializing output.

