from django.shortcuts import render
from django.forms import formset_factory
from . import forms
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


def form_set_post(request):
    TestFormSet = formset_factory(forms.FormSetPost, extra=3)
    