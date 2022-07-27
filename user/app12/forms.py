from django import forms
from app12.models import User
class Newuserform(forms.ModelForm):
    class Meta():
        model=User
        fields="__all__"