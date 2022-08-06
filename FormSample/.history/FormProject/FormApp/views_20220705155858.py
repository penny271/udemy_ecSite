from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory
from . import forms
from .models import ModelSetPost
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_page(request):
    #- forms.py から userInfoをインスタン化する
    form = forms.UserInfo()
    if request.method == 'POST':
        # Formで送られたデータを取り出す
        form = forms.UserInfo(request.POST)
        if form.is_valid():# バリデーション(フィールドが正しいかチェック)
            print('バリデーション成功')
            # print(f'name: {form.cleaned_data["name"]},mail: {form.cleaned_data["mail"]} age: {form.cleaned_data["age"]}')
            #- form.cleaned_data[‘subject’] # フォームの中の情報を扱う
            print(form.cleaned_data)
        #! invalidでもPOSTでフォームのデータは渡ってくる
        else:
            print('invalid form')
    return render(
        request, 'formapp/form_page.html', context={
            'form': form,
        }
    )

def form_post(request):
    form = forms.PostModelForm()
    if request.method == 'POST':
        form = forms.PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(
        request, 'formapp/form_post.html', context= {'form':form}
    )

#- Formsetを利用すると、同じFormを複数個、簡単に画面上に表示することができる。
def form_set_post(request):
    # インスタンス化の一歩手前
    #- # extraでFormを画面上にいくつ表示す るか定義
    TestFormset = formset_factory(forms.FormSetPost, extra=3)
    # インスタンス化
    #- or の用法 - 左の値が存在すれば左の値を使い、そうでなければ右の値を使う
    formset = TestFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
            # print(form) #! HTMLが返ってくる
    return render(request, 'formapp/form_set_post.html',
    context = {'formset': formset}
    )

def modelform_set_post(request):
    #- from .models import ModelSetPost をimportしている
    TestFormSet = modelformset_factory(ModelSetPost, fields='__all__', extra=3)
    # TestFormSet = modelformset_factory(ModelSetPost, form=forms.ModelFormSetPost, extra=3)
    #- queryset=ModelSetPost.objects.filter(id__gt=3) で
    #- filterする
    formset = TestFormSet(request.POST or None, queryset=ModelSetPost.objects.filter(id__gt=8))
    if formset.is_valid():
        formset.save()
        print('modelform_set_post: ',formset.cleaned_data)
    return render(request, 'formapp/modelform_set_post.html', context={
        'formset':formset,
    })

# def upload_sample(request):
#     #- nameで指定した値をrequest.FILESで取得しています。
#     if request.method == 'POST' and request.FILES['upload_file']:
#         # 送られたファイルの取り出し
#         upload_file = request.FILES['upload_file']
#         # インスタンス化
#         #! 要import => from django.core.files.storage import FileSystemStorage
#         fs = FileSystemStorage() # ファイルを保存する
#         file_path = os.path.join('upload', upload_file.name)
#         file = fs.save(file_path, upload_file)
#         uploaded_file_url = fs.url(file)
#         return render(request, 'formapp/upload_file.html', context = {
#             'uploaded_file_url': uploaded_file_url,
#         })
#     return render(request, 'formapp/upload_file.html')

def upload_sample(request):
    if request.method == 'POST' and request.FILES['upload_file']:
        # 送られたファイルの取り出し
        upload_file = request.FILES['upload_file']
        fs = FileSystemStorage() # ファイルを保存する
        file_path = os.path.join('upload', upload_file.name)
        file = fs.save(file_path, upload_file)
        uploaded_file_url = fs.url(file)
        return  render(request, 'formapp/upload_file.html', context={
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'formapp/upload_file.html')

def upload_model_form(request):
    user = None
    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
    else:
        form = forms.UserForm()
    return render(request, 'formapp/upload_model_form.html', context = {'form':form, 'user':})