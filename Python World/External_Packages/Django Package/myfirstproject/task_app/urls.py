from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_admin_login, name='login'),

]