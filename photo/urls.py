from django.urls import path

from . import views

app_name = 'photo'
urlpatterns = [
    # ex: /
    path('', views.AlbumLV.as_view(), name='index'),

    # ex: /album/, same as /
    path('album/', views.AlbumLV.as_view(), name='album_list'),

    # ex: /album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # ex: /photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

    # ex: /album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    # ex: /album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # ex: /album/99/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),

    # ex: /album/99/delete/
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

    # ex: /photo/add/
    path('photo/add/', views.PhotoCreateView.as_view(), name='photo_add'),

    # ex: /photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # ex: /photo/99/update/
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo_update'),

    # ex: /photo/99/delete/
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),

]
