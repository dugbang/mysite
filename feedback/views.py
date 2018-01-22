from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .forms import FeedbackForm


def create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})


def edit(request, feedback_id):
    fb = Feedback.objects.get(pk=feedback_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=fb)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm(instance=fb)

    return render(request, 'feedback/feedback.html', {'form': form})


def list(request):
    fb = Feedback.objects.all()
    return render(request, 'feedback/feedbacklist.html', {'feedbacks': fb})

