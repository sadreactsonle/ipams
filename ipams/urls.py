from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('login/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('records/', include('records.urls'))
]
