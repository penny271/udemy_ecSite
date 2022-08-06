from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):
    
    #- 情報の上書き、追加
    name = forms.CharField(label='名前')

    class Meta:
        model = Students
        fields = '__all__'

