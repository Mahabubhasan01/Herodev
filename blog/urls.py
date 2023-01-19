from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('categories', views.Blog_cat, name='categories'),
    path('category/<str:cat>/', views.FilterBy_cat, name='category'),
    path('<str:category>/<str:title>/P<pk>[0-9a-f-]',
         views.Blog_detail_Page, name='page_details'),
]
