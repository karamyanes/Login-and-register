from django.urls import path, include
from . import api
# from .api import TransactionListAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register('question', api.QuestionView)
router.register('answer', api.AnswerView)
router.register('game', api.GameView)



urlpatterns = [
    #path('answer/', include(router.urls)),
    path('game/question/answer', include(router.urls)),
   #  path('question/',include(router.urls)),
	# path("transaction/list/", TransactionListAPI.as_view()),
]
