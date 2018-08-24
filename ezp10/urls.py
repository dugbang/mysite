from django.urls import path

from . import views

app_name = 'ezp10'
urlpatterns = [
    path('plant/', views.PlantLV.as_view(), name='plant'),

    # path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    path('plant_j/<int:pk>', views.plant_json, name='detail_j'),
    path('plant_j/add', views.plant_add_json, name='create_j'),
]
