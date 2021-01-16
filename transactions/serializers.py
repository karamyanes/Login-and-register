from .models import Transaction
from rest_framework import serializers


class TransactionListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = "__all__"
