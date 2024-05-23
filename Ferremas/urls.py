from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Ferremas_pri.urls')),
    path('user/', include('login.urls')),
    path('user/', include('django.contrib.auth.urls')),
]
    
