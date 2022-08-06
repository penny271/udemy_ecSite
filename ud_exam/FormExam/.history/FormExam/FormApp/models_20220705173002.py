from django.db import models

# Create your models here.
class Students(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    picture = models.FileField(upload_to='student/')

    class Meta:
        db_table= 'students'
