import json
import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ezp10.models import Plant
from ezp10.serializers import PlantSerializerFunc

ezp10_logger = logging.getLogger(__name__)


class PlantLV(ListView):
    model = Plant
    template_name = 'ezp10/plant_list.html'


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_plants(request, pk):
    try:
        plant = Plant.objects.get(pk=pk)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single plant
    if request.method == 'GET':
        serializer = PlantSerializerFunc(plant)
        return Response(serializer.data)
    # delete a single plant
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single plant
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_plants(request):
    # get all puppies
    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializerFunc(plants, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == 'POST':
        # data = {
        #     'name': request.data.get('name'),
        # }
        # data = json.loads(request.body.decode("utf-8"))
        data = json.loads(request.body)
        ezp10_logger.debug(data)
        serializer = PlantSerializerFunc(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

