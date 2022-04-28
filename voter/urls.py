from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register_save/', views.register_save, name='register-save'),
    path('login/', views.login, name = 'login'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('aftervote/', views.aftervote, name='aftervote'),
]
