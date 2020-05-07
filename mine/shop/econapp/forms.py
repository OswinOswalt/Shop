from django import forms
from django.contrib.auth import authenticate


class UserloginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':  "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username.strip(), password=password.strip())
            if not user:
                raise forms.ValidationError('Такого пользователя нет')
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return super(UserloginForm, self).clean(*args, **kwargs)
