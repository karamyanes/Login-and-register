from django.urls import path, include
from . import api
# from .api import TransactionListAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register('transactions', api.TransactionView)

urlpatterns = [
    path('', include(router.urls)),
	# path("transaction/list/", TransactionListAPI.as_view()),
]
