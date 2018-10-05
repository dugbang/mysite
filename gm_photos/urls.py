from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'gm_photos'
urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('upload/', views.create, name='create'),
    path('upload/', views.PhotoCreateView.as_view(), name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
