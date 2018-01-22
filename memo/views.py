from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Memo


class MemoList(ListView):
    model = Memo


class MemoDetail(DetailView):
    model = Memo
