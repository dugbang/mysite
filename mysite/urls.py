"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # path('rest_app/', include('rest_app.urls')),

    # path('ezp_api/', include('ezp_api.urls')),
    path('ezp10/', include('ezp10.urls')),
    path('gm_photos/', include('gm_photos.urls')),

    path('photo/', include('photo.urls')),
    path('blog/', include('blog.urls')),
    path('bbs/', include('bbs.urls')),
    path('memo/', include('memo.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('polls/', include('polls.urls')),
    path('feedback/', include('feedback.urls')),
    path('home/', include('home.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
