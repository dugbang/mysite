from django.http import HttpResponse
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

