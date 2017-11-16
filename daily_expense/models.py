from audioop import reverse

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    expense_date = models.DateTimeField()
    expense_details = models.CharField(null=True, blank=True, max_length=200, help_text="Enter expense details")
    expense_amount  = models.FloatField(null=True, help_text="Enter expense amount")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.expense_details
