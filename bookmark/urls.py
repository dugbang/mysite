from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),


    path('add/', views.BookmarkCreateView.as_view(), name="add"),

    # ex: /change/
    path('change/', views.BookmarkChangeLV.as_view(), name="change"),

    # ex: /99/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update"),

    # ex: /99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete"),

]
