from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /
    path('', views.PostLV.as_view(), name='index'),  # 1

    # ex: /post/ (same as /)
    path('post/', views.PostLV.as_view(), name='post_list'),  # 2

    # ex: /post/ex/
    path('post/ex/<slug:slug>/', views.PostDV.as_view(), name='post_detail'),  # 3

    # ex: /archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),  # 4

    # ex: /2017/
    path('<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),  # 5

    # ex: /2017/nov/
    path('<int:year>/<int:month>/', views.PostMAV.as_view(), name='post_month_archive'),  # 6

    # ex: /2017/nov/10/
    path('<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),  # 7

    # ex: /today/
    path('today/', views.PostTAV.as_view(), name='post_today_archive'),
]
