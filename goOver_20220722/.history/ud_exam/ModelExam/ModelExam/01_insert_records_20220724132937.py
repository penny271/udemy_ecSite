#- ★順番どおりにimportしていかないと以下のようなエラーが出る
#! django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
#- setup()してからモデルを呼び出す!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

# from ModelApp.models import Students, TestResults, Tests, Classes
# from random import randint

# from ModelApp.models import Students, Tests_results, Tests, Classes
# from random import randint

class_names = ['Class' + c for c in 'ABCDEFGHIJ']
student_names = ['student' + s for s in 'ABCDEFGHIJ']

ref_list = ['A','B','C','D','E','F','G','H','I','J']
subjects = ['数学','英語','国語']

for i in class_names:
    print(i)

for i in student_names:
    print(i)

# for class_name in ref_list:
#     class_info = Classes(
#         name = class_name
#     )
#     class_info.save()
#     for student_name in ref_list:
#         student = Students(
#             class_id = class_info,
#             name = student_name,
#             grade = 1,
#         )
#         student.save()
#         for subject in subjects:
#             test = Tests(
#                 name = subject,
#             )
#             test.save()
#             for test_result_info in subjects:
#                 test_result = Tests_results(
#                     student = student,
#                     test = test,
#                     score = randint(50,100),
#                 )
#                 test_result.save()









