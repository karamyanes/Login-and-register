from django.db.models import Q
from rest_framework import generics, permissions, viewsets
from .models import Transaction
from .serializers import TransactionListSerializer


# class TransactionListAPI(generics.ListAPIView):
# 	serializer_class = TransactionListSerializer
# 	permission_classes = [
# 		permissions.IsAuthenticated
# 	]

# 	def get_queryset(self, *args, **kwargs):
# 		queryset = Transaction.objects.all()
# 		query = self.request.GET.get("q")

# 		return queryset


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer
