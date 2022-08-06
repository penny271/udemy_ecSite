from django.db import models
from django.forms import CharField

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'

    def __str__(self):
        return self.name

class Tests(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tests'

    def __str__(self):
        return self.name

class Students(models.Model):
    name = name = models.CharField(max_length=50)
    class_id = models.ForeignKey("Classes",on_delete=models.CASCADE)
    grade = models.IntegerField()

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name

class Tests_results(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    test = models.ForeignKey('Tests', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tests_results'

    def __str__(self):
        return f'test_score: {self.score}'