from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='accounts-register'),
    path('get/all', views.get_all_accounts, name='accounts-get-all'),
    path('login/', views.LoginView.as_view(), name='accounts-login'),
    path('logout/', views.logout, name='accounts-logout'),
]
