from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='records-index'),
    path('view/<int:record_id>', views.ViewRecord.as_view(), name='records-view'),
    path('create/', views.Create.as_view(), name='records-create'),
    path('update/<int:record_id>', views.Update.as_view(), name='records-update'),
    path('uploadexcel/', views.ParseExcel.as_view(), name='records-upload'),
]
