from tkinter.tix import Tree
from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Sales(models.Model):
    fee = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = updateat