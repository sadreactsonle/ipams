from django.conf.urls.static import static
from django.urls import path

from ipams import settings
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='records-index'),
    path('record/<int:record_id>', views.ViewRecord.as_view(), name='records-view'),
    path('add/', views.Add.as_view(), name='records-add'),
    path('uploadexcel/', views.ParseExcel.as_view(), name='records-upload'),
    path('downloadformat/', views.download_format, name='records-download-format'),
    path('download/abstract/<int:record_id>', views.download_abstract, name='records-download-abstract'),
    path('user/', views.MyRecordsView.as_view(), name='records-myrecords'),
    path('pending/', views.PendingRecordsView.as_view(), name='records-pending'),
    path('approved/', views.ApprovedRecordsView.as_view(), name='records-approved'),
    path('declined/', views.DeclinedRecordsView.as_view(), name='records-declined'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
