from django.urls import path, re_path
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /
    path('', views.PostLV.as_view(), name='index'),  # 1

    # ex: /post/ (same as /)
    path('post/', views.PostLV.as_view(), name='post_list'),  # 2

    # ex: /archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),  # 4

    # ex: /today/
    path('today/', views.PostTAV.as_view(), name='post_today_archive'),

    # ex: /post/slug/
    path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail'),  # 3
    # re_path('post/(?P<slug>[\w-_]+)/', views.PostDV.as_view(), name='post_detail'),  # 3

    # ex: /2017/nov/
    path('<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),  # 6

    # ex: /2017/nov/10/
    path('<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),  # 7

    # ex: /2017/
    path('<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),  # 5

    # ex: /tag/
    path('tag/', views.TagTV.as_view(), name='tag_cloud'),

    # ex: /tag/tagname/
    path('tag/<tag>/', views.PostTOL.as_view(), name='tagged_object_list'),

    # ex: /search/
    path('search/', views.SearchFormView.as_view(), name='search'),

    # ex: /add/
    path('add/', views.PostCreateView.as_view(), name="add"),

    # ex: /change/
    path('change/', views.PostChangeLV.as_view(), name="change"),

    # ex: /99/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),

    # ex: /99/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),
]
