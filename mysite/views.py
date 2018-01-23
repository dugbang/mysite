from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render


# --- TemplateView
class HomeView(TemplateView):  # 1
    template_name = 'home.html'  # 2


def index(request):
    return render(request, 'home.html')

