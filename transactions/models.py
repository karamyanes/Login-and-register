from django.db import models
from datetime import datetime


class Type(models.Model):
    type = (
        (1, "Expense"),
        (2, "Income"),
    )
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.type


class Transaction(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    amount = models.FloatField(null=False, blank=False, default=None)
    type = models.IntegerField(choices=Type.type, default=1, blank=False)  # added Expense size as default

    def __str__(self):
        return self.name
