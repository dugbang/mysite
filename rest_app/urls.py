from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from . import views

# router = routers.DefaultRouter()
# router.register(r'persons', views.PersonViewSet)

app_name = 'rest_app'
urlpatterns = [
    path('', views.PersonList.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/doc/', get_swagger_view(title='Rest API Document')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
