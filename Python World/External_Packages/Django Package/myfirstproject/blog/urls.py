from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='hello'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello_user, name='hello_user'),
    path('post/<int:id_number>/', views.post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),
]
