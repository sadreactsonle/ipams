from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from . import forms
from .models import User


class RegisterView(View):
    name = 'accounts/register.html'

    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, self.name, {'form': form, 'hide_profile': True})

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_password()
            if password:
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('/')
            error_message = 'Password did not match!'
        else:
            if not form.cleaned_data.get('username'):
                error_message = 'Username not available'
            elif not form.cleaned_data.get('email'):
                error_message = 'That E-mail is already in used by another user'
            else:
                error_message = 'Invalid form'
        form = forms.RegistrationForm()
        return render(request, self.name, {'form': form, 'error_message': error_message, 'hide_profile': True})


class LoginView(View):
    name = 'accounts/index.html'

    def get(self, request):
        form = forms.LoginForm()
        if request.user.is_authenticated:
            return redirect('records-index')
        error_message = None
        if request.GET.get('next'):
            error_message = 'Login Required'
        return render(request, self.name, {'form': form, 'error_message': error_message, 'hide_profile': True})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('records-index')
        form = forms.LoginForm()
        return render(request, self.name, {'error_message': 'Invalid Username/Password',
                                           'form': form, 'hide_profile':True})


def logout(request):
    auth_logout(request)
    return redirect('/')


def get_all_accounts(request):
    accounts = User.objects.all()
    data = []
    for account in accounts:
        data.append([
            '',
            account.pk,
            str(account.username),
            str(account.last_name)+', '+str(account.first_name),
            account.role,
        ])
    return JsonResponse({'data': data})
