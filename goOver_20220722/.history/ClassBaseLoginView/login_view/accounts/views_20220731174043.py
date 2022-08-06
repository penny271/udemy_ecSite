



# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

# class UserLoginView(FormView):
#     template_name = 'user_login.html'
#     form_class = UserLoginForm

#     def post(self, request, *args, **kwargs):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)
#         #- user_login.html で 取得する
#         #- <input type="hidden" name="next" value="{{ request.GET.next }}">
#         next_url = request.POST['next']
#         if user is not None and user.is_active:
#             login(request,user)
#             print('login成功!!')
#         else:
#             print('login失敗!!')
#         if next_url:
#             return redirect(next_url)
#         return redirect('accounts:home')

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    #- # This method is called when valid form data has been POSTed.
    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        #-セッションの保存時間を引数の時間(秒)に変更する。引数が0の 場合、ブラウザを閉じるとセッションがなくなる。もし value が datetime または timedelta オブジ ェクトならば、指定された日時に破棄される
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)

# class UserLogoutView(View):

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('accounts:user_login')

class UserLogoutView(LogoutView):
    pass

#^ djangoのヴァージョンアップでログインしていない場合は設定なしで
#^ ログイン画面へ飛ばす仕様になっている模様。
#- ログインが必要なViewにデコレータを付ける方法
# @method_decorator(login_required, name='dispatch')
class UserView(LoginRequiredMixin,TemplateView):
    template_name = 'user.html'
    print('A')

    #- dispatchは必ず実行されるメソッド
    # @method_decorator(login_required)
    def dispatch(self,  *args, **kwargs):
        print('dispatch')
        return super().dispatch( *args, **kwargs)
