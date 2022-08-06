from django import forms
from django.core import validators

from .models import Post


#- 自作バリデーター
def check_name(value):
    if value=='あああああ':
        raise validators.ValidationError('その名前は登録できません')  # type: ignore


class UserInfo(forms.Form):
    #- 自作のバリデーションを適用
    name = forms.CharField(label='名前', min_length=5, max_length=10, validators=[check_name])
    # name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name_class','placeholder':'sample_name'}))
    # - フィールドに対して、validators=[]で属性を追加する field ~ forms.CharField(validators = [○○]) # ○○には、djangoのライブラリ内のクラス  自作の関数を入れる
    age = forms.IntegerField(label='年齢', validators=[validators.MinValueValidator(20, message="20以上にしましょう")])
    mail = forms.EmailField(
        label='メールアドレス',
        widget=forms.TextInput(attrs={'class':'mail-class','placeholder':'sample@mail.com'})
    )
    verify_mail = forms.EmailField(
        label='メールアドレス再入力',
        widget=forms.TextInput(attrs={'class':'mail-class','placeholder':'sample@mail.com'})
    )
    is_married = forms.BooleanField(initial=True)
    birthday = forms.DateField(initial='1990-10-10')
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, '正社員'),
        (2, '自営業'),
        (3, '学生'),
        (4, '無職'),
    ), widget=forms.RadioSelect
                            )
    hobbies = forms.MultipleChoiceField(choices=(
        (1, 'スポーツ'),
        (2, '読書'),
        (3, '映画鑑賞'),
        (4, 'その他'),
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobbies'].widget.attrs['class'] = 'hobbies_class'

#- 1.フィールドごとのバリデーション用のメソッドを定義する
    def clean_homepage(self):
        homepage = self.cleaned_data['homepage']
        if not homepage.startswith('https'):
            #- ビュー側の画面上にメッセージが表示され、request.POSTは送信されない
            raise forms.ValidationError('ホームページのurlはhttpsのみ!!')

#- 3. cleanメソッドを定義して、複数のフィールドの値をチェックする
# cleanメソッドは、親クラス(forms.Form)が持っているメソッドをオーバーライド（上書き）している
    def clean(self):
        print(super().clean())
        cleaned_data = super().clean()
        mail = cleaned_data['mail']
        vefify_mail = cleaned_data['verify_mail']
        if mail != vefify_mail:
            raise forms.ValidationError('メアドが一致していない!')

class PostModelForm(forms.ModelForm):

    memo = forms.CharField(widget=forms.Textarea(attrs={'row'=30}))

    class Meta:
        model = Post
        # fields = '__all__'
        # fields = ['name', 'title']
        exclude = ['title']



