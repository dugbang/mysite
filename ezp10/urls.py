from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ezp10 import views

app_name = 'ezp10'
urlpatterns = [
    # path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # path('plant_j/<int:pk>', views.plant_json, name='detail_j'),
    # path('plant_j/add', views.plant_add_json, name='create_j'),
    # path('api-f/plant/<int:pk>', views.get_delete_update_plants, name='plant_api_get'),
    # path('api-f/plant/', views.get_post_plants, name='plant_api_post').

    path('api/plant/', views.PlantList.as_view(), name='api_plant_list'),
    path('api/plant/<int:pk>', views.PlantDetail.as_view(), name='api_plant_detail'),

    path('api/report/', views.ReportList.as_view(), name='api_report_list'),
    path('api/controller/<pk>/', views.ControllerDetail.as_view(), name='api_controller_detail'),

    # path('api/capture/', views.CaptureList.as_view(), name='capture_list'),
    # path('api/capture/<int:pk>', views.CaptureDetail.as_view(), name='capture_detail'),

    path('plant/', views.PlantLV.as_view(), name='plant'),
    path('capture/', views.CaptureLV.as_view(), name='capture_list'),
    # path('capture/<int:pk>', views.CaptureDV.as_view(), name='capture_detail'),
    path('capture/upload/', views.CaptureCreateView.as_view(), name='capture_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
