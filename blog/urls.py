from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('categories', views.Blog_cat, name='categories'),
    path('b', views.Blog_detail, name='blog_detail'),
]
