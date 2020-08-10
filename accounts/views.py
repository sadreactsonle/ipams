from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from . import forms


class LoginView(View):
    name = 'accounts/index.html'

    def get(self, request):
        form = forms.LoginForm()
        if request.user.is_authenticated:
            return redirect('records-index')
        return render(request, self.name, {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'records/index.html', {'form': form})
        form = forms.LoginForm()
        return render(request, self.name, {'error_message': 'Invalid Username/Password', 'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
