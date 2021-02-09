from django.db.models import Q
from rest_framework import generics, permissions, viewsets
from .models import Game
from .models import UserQuestionHistory
from .models import Player
from .models import Question
from .models import Answer
from .models import Result
from .serializers import QuestionListSerializer
from .serializers import AnswerListSerializer
from .serializers import GameListSerializer





# class TransactionListAPI(generics.ListAPIView):
# 	serializer_class = TransactionListSerializer
# 	permission_classes = [
# 		permissions.IsAuthenticated
# 	]

# 	def get_queryset(self, *args, **kwargs):
# 		queryset = Transaction.objects.all()
# 		query = self.request.GET.get("q")

# 		return queryset


class QuestionView(viewsets.ModelViewSet):
	"""
	A simple ViewSet for view, edit and delete Transactions.
	"""
	queryset = Question.objects.all()
	serializer_class = QuestionListSerializer
	#permission_classes = [permissions.IsAuthenticated] #this permission we need to be sure that only permited user can use this url


class GameView(viewsets.ModelViewSet):
	"""
	A simple ViewSet for view, edit and delete Transactions.
	"""
	queryset = Game.objects.all()
	serializer_class = GameListSerializer
	#permission_classes = [permissions.IsAuthenticated] #this permission we need to be sure that only permited user can use this url


class AnswerView(viewsets.ModelViewSet):
	"""
	A simple ViewSet for view, edit and delete Transactions.
	"""
	queryset = Answer.objects.all()
	serializer_class = AnswerListSerializer
	#permission_classes = [permissions.IsAuthenticated] #this permission we need to be sure that only permited user can use this url