from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.PostLV.as_view(), name='index'),  # 1

    # ex: /post/ (same as /)
    url(r'^post/$', views.PostLV.as_view(), name='post_list'),  # 2

    # ex: /post/ex/
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),  # 3

    # ex: /archive/
    url(r'^archive/$', views.PostAV.as_view(), name='post_archive'),  # 4

    # ex: /2017/
    url(r'^(?P<year>\d{4})/$', views.PostYAV.as_view(), name='post_year_archive'),  # 5

    # ex: /2017/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', views.PostMAV.as_view(), name='post_month_archive'),  # 6

    # ex: /2017/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', views.PostDAV.as_view(), name='post_day_archive'),  # 7

    # ex: /today/
    url(r'^today/$', views.PostTAV.as_view(), name='post_today_archive'),

]
