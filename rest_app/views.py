from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, generics

from rest_app.models import Person
from rest_app.serializers import PersonSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
