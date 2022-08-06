from django.db import models
from django.utils import timezone
import pytz

class BaseMeta(models.Model):
    create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))
    update_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone('Asia/Tokyo')))

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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#- 外部キー
class Students(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=20)
    #- Schoolsが1で Studentsが多 の関係 lec.123
    school = models.ForeignKey(
        'Schools', on_delete=models.CASCADE
    )
    prefecture = models.ForeignKey(
        'Prefectures', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'students'
        unique

