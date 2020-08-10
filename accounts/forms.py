from django import forms
from django.contrib.auth import authenticate

from accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=(('rdco', 'rdco'), ('ktto', 'ktto'), ('teacher', 'teacher'), ('student', 'student')))
    password = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password')

    def cleaned_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            return None
        return password
