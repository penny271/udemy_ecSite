from django.forms import forms
.models import Students


class Students_form(forms.ModelForm):

    class Meta:
        model=