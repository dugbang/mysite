from django.urls import path

from . import views

app_name = 'gm_photos'
urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('<int:pk>/', views.detail, name='detail'),
    path('upload/', views.create, name='create'),
]
