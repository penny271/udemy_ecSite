from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

