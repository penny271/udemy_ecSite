#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Classes

student_1 = Students.objects.get(pk=1)
print(student_1)
# print(dir(student_1))

for result in student_1.testsresults_set.all():
    print(dir(result))

    print(result.student.name,result.test.name, result..first().result.name,result.testsresults_set.first().score, )

# print(student_1.name, student_1.testsresults_set.first().test.name,student_1.testsresults_set.first().score, )

from django.db.models import Max, Min, Avg, Count, Sum

# test_result_list = TestsResults.objects.values('score', 'student', 'test')