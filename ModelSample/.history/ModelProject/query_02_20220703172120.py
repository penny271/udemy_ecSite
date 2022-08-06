# select_foreign_table.py

import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Students, Person

# 全件取得 all()
# print(Students.objects.all())

# IN
ids = [13,14,15]
# print(Students.objects.filter(pk__in=ids))

# contain 部分一致
# like '%〇〇%'  SQL
print(Students.objects.filter(name__contains))