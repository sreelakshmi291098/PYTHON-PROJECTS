from django import forms
class Register(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField()
    Text=forms.CharField()


