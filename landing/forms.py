from django import forms

class MyForm(forms.Form):
    NAME = forms.CharField()
    EMAIL = forms.EmailField()
    MESSAGE = forms.CharField()