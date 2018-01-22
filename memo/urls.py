from django.urls import path

from . import views

app_name = 'memo'
urlpatterns = [
    path('', views.MemoList.as_view(), name='index'),
    path('<int:pk>/', views.MemoDetail.as_view(), name='detail'),
]
