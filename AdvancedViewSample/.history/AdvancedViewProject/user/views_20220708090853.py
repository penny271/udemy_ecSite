import profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm, ProfileForm, LoginForm
#- passwordが合っているか確認
from django.contrib.auth import authenticate,login

# Create your views here.
def user_list(request):
    return render(request, 'user/user_list.html', context={})

def index(request):
    return render(request, 'user/index.html')

def register(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save() #ユーザー登録
        user.set_password(user.password) #パスワードを暗号化して保存する
        user.save() #ユーザーを保存する
        #- データベースに保存ではなく、メモリ上に保存 commit=False
        profile = profile_form.save(commit=False)
        #! profileはuserと1対1で紐付いているので
        #! .userで設定すると外部キーとしてユーザーを登録することができる
        profile.user = user
        profile.save() #- ハードディスク上に保存
    return render(request, 'user/register.html', context={
        'user_form':user_form,
        'profile_form': profile_form,
    })

def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        #- passwordが合っているか確認 - importした関数使用
        user = authenticate(username=username, password=password)
        if user:
            #- userが有効な場合
            if user.is_active:
                login(request, user)
                return redirect('user:index')
            else:
                return HttpResponse('アカウントがアクティブでないです。')
        #- userが存在しない場合
        else:
            return HttpResponse('ユーザーが存在しません')
            