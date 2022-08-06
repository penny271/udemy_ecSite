from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    #- mediaフォルダもsutdent/フォルダも作る必要なし
    #- settings.pyで保存場所を指定済みのため
    picture = models.FileField()

    class Meta:
        db_table= 'students'
