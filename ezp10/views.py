import json
import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ezp10.models import Plant, Capture, Report, Controller
from ezp10.serializers import PlantSerializer, CaptureSerializer, ReportSerializer, ControllerSerializer
from mysite.views import LoginRequiredMixin

ezp10_logger = logging.getLogger(__name__)


class PlantLV(ListView):
    model = Plant
    # template_name = 'ezp10/plant_list.html'


class CaptureLV(ListView):
    model = Capture
    # template_name = 'ezp10/capture_list.html'


class CaptureDV(DetailView):
    model = Capture
    # template_name = 'ezp10/capture_detail.html'


class CaptureCreateView(CreateView):
    """
    class CaptureCreateView(LoginRequiredMixin, CreateView):
    LoginRequiredMixin >> login check...
    """
    model = Capture
    fields = ('plant', 'controller', 'image', 'create_at')
    success_url = reverse_lazy('ezp10:capture_upload')

    # template_name = 'ezp10/capture_form.html'

    # @csrf_exempt
    def form_valid(self, form):
        # form.instance.owner = self.request.user
        return super(CaptureCreateView, self).form_valid(form)


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ControllerDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset 에 대한 정보를 갱신해야 할 수 있음. pk 정보가 아니라 serial 로 정보확인해야 함... 어떻게?
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer


# generics 에 목록과 생성 API 가 정의되어 있다
class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


# generics 에 목록과 생성 API 가 정의되어 있다
class CaptureList(generics.ListCreateAPIView):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer


# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class CaptureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_plants(request, pk):
    try:
        plant = Plant.objects.get(pk=pk)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single plant
    if request.method == 'GET':
        serializer = PlantSerializer(plant)
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
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == 'POST':
        # data = {
        #     'name': request.data.get('name'),
        # }
        # data = json.loads(request.body.decode("utf-8"))
        data = json.loads(request.body)
        ezp10_logger.debug(data)
        serializer = PlantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

