from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login',views.custom_login),#เรียกใช้ def ชื่อ custom_login
    path('logout/',views.logout_view),
    path('register/', views.register_view, name='register'),
    
]