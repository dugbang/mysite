from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.views import TaggedObjectList

from blog.models import Post


# -- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# -- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


# -- DetailView
class PostDV(DetailView):
    model = Post


# -- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    allow_future = True


class PostYAV(YearArchiveView):
    # queryset = Post.objects.all()
    model = Post
    date_field = "modify_date"
    make_object_list = True
    allow_future = True
    # model = Post
    # date_field = 'modify_date'
    # make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'
    allow_future = True


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'
    allow_future = True


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
    allow_future = True
