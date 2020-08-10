from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='accounts-index'),
    path('login/', views.LoginView.as_view(), name='accounts-login'),
    path('logout/', views.logout, name='accounts-logout'),
]
