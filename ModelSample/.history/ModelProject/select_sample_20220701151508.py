import os

#- djangoを使ったプロジェクトを読み込むための記述
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
#- ModuleNotFoundError: No module named 'django'
#! vscode のインテープレターの問題なので、djangoが使える環境を選択する
#! ※ Terminalが djangoが入っている仮想環境であっても上記を揃える必要あり!
from django import setup
setup()

from ModelApp.models import Person

# すべて取得
persons = Person.objects.all()
for person in persons:
    print(person.id, person, person.salary)

# person = Person.objects.get(first_name='Taro')
# person = Person.objects.get(first_name='taro')

print(person.id, person, person)
