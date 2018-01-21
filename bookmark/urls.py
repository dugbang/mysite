from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path(r'^?P<pk>\d+/$', views.BookmarkDV.as_view(), name='detail'),
    # path(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    # path(r'^bookmark/?P<pk>\d+/$', views.BookmarkDV.as_view(), name='detail'),
]
