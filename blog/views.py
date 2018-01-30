from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q

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


# -- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=schWord)
            | Q(description__icontains=schWord)
            | Q(content__icontains=schWord)).distinct()

        context = {'form': form, 'search_term': schWord, 'object_list': post_list}

        return render(self.request, self.template_name, context)
