from django.urls import path
from login import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('register_staff/', views.register_staff, name='register_staff'),
    path('logout/', views.logout_view, name='logout'),
]
