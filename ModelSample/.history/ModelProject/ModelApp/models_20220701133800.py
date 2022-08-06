from tkinter.tix import Tree
from django.db import models
from django.utils import timezone

# Create your models here.

class BaseMeta(models.Model):
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

#- models.Modelを継承する
# class Person(models.Model):
#- BaseMetaを継承する
class Person(BaseMeta):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True) #- デフォルトはFalse Trueでnullの値を入れることができる
    memo = models.TextField()
    web_site = models.URLField(null=True, blank = True) #- None, '' を入れることができる
    #! BaseMeta で継承したため不要
    # crate_at = models.DateTimeField(default = timezone.datetime.now) #- 作成日時

    class Meta:
        db_table = 'person'
        index_together = [['first_name', ]]