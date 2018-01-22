from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'bbs'
urlpatterns = [
    # path('', views.bbs_list),
    # path('<int:pk>/', views.bbs_detail),

    path('', views.BbsList.as_view()),
    path('<int:pk>/', views.BbsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
