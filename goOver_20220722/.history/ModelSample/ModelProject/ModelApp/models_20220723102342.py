from django.db import models
from django.utils import timezone
import pytz

class BaseMeta(models.Model):
    create_at = models.DateField(default=timezone.datetime.now)
    update_at = models.DateField(default=timezone.datetime.now)

    class Meta:
        abstract=True

# Create your models here.
class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True) #処理の高速化 データの容量が大きくなる
    salary = models.FloatField(null = True)
    memo = models.TextField()
    web_site = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        ordering = ['salary']

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     birthday = models.DateField(default='1900-01-01')
#     email = models.EmailField(db_index=True)
#     salary = models.FloatField(null=True) #- デフォルトはFalse Trueでnullの値を入れることができる
#     memo = models.TextField()
#     web_site = models.URLField(null=True, blank = True) #- None, '' を入れることができる
#     create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))


class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True) #処理の高速化 データの容量が大きくなる
    salary = models.FloatField(null = True)
    memo = models.TextField()
    web_site = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        ordering = ['salary']