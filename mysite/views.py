from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView, View
from django.shortcuts import render


# --- TemplateView
class HomeView(TemplateView):  # 1
    template_name = 'home.html'  # 2

    # def get(self, request):
    #     # 뷰 로직 작성
    #     return render(request, 'home.html')


def index(request):
    return render(request, 'home.html')


# --- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
