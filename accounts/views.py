from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    name = 'accounts/index.html'

    def get(self, request):
        form = forms.LoginForm()
        return render(request, self.name, {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
        return render(request, 'records/index.html', {'form': form})
