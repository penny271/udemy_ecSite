from django.shortcuts import render
#- forms を使えるようにする - forms.pyの情報がmodels.pyを更新したものだから
from . import forms
from .models import Students

# Create your views here.




def insert_student(request):
    #! request.FILESも入れる
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None )
    if insert_form.is_valid():
        insert_form.save()
        #- 送信後、初期化 inputの中身を空にする
        insert_form = forms.StudentInsertForm()
    return render(request, 'form_app/insert_student.html', context={
        'insert_form' : insert_form,
    })

#- Student情報を全件リスト表示する .modelsからStudentsを読み込む import
def students_list(request):
    students = Students.objects.all()
    return render(
        request, 'form_app/students_list.html', context={
            'students':students,
        }
    )

def update_student(request, id):
    student = Students.objects.get(id=id)
    update_form = forms.StudentUpdateForm(
        initial={
            'name': student.name,
            'age': student.age,
            'grade': student.grade,
            'name': student.name,
        }
    )
