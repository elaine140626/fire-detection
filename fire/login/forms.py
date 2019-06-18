from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, min_length=1, widget=forms.TextInput)
    password = forms.CharField(label='密码', max_length=256, min_length=1, widget=forms.PasswordInput)
