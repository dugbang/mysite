from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from django.http import HttpResponse

from gm_photos.forms import PhotoForm
from .models import Photo


def hello(request):
    return HttpResponse('안녕하세요!')


def detail(request, pk):
    photo = photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )

    return HttpResponse('\n'.join(messages))


def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'gm_photos/edit.html', ctx)


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('image', 'content')
    success_url = reverse_lazy('gm_photos:create')

    template_name = 'gm_photos/edit.html'

    # @csrf_exempt
    def form_valid(self, form):
        # form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

