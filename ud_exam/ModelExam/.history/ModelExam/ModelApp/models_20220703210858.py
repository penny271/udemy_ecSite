from django.db import models

# Create your models here.

class Test_results(models.Model):
    score = models.IntegerField()
    tests = models.ForeignKey('tests',delete_on=models.CASCADE)
    students = models.ForeignKey('')


class Tests(models.Model):
    name = models.CharField(max_length=50)