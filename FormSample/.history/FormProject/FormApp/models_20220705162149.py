from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    memo = models.CharField(max_length=255)

class ModelSetPost(models.Model):
    title = models.CharField(max_length=255)
    memo = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    #- ファイルの保存先ディレクトリの作成、指定
    # picture = models.FileField(upload_to='picture/')
    picture = models.FileField(upload_to='picture/')