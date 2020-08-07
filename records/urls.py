from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='records-index'),
    path('create/', views.Create.as_view(), name='records-create'),
    path('uploadexcel/', views.ParseExcel.as_view(), name='records-upload'),
]
