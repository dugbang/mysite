from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:_id>/', views.BookmarkDV.as_view(), name='detail'),
    # path(r'^?P<pk>\d+/$', views.BookmarkDV.as_view(), name='detail'),
    # <int:question_id>/
    # path(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    # path(r'^bookmark/?P<pk>\d+/$', views.BookmarkDV.as_view(), name='detail'),
]
