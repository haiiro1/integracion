from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('Ferremas_pri.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('Ferremas_pri.urls')),
    path('user/', include('login.urls')),
    path('user/', include('django.contrib.auth.urls')),

]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)