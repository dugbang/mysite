import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from ezp10.models import Plant


class PlantLV(ListView):
    model = Plant

    template_name = 'ezp10/plant_list.html'


def plant_json(request, pk=None):
    entries = Plant.objects.get(id=pk)
    data = entries.dic()

    return HttpResponse(json.dumps(data), content_type="application/json")


def plant_add_json(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        # TODO; 동일한 name 이 있을 때 무시하거나 예외발생 필요. create 보다는 put 이 더 맞지 않나?
        # TODO; 장고 REST 프래임워크를 확인해볼 필요가 있음.
        print(received_json_data)
        if 'name' not in received_json_data:
            return HttpResponseBadRequest('json data error...')

        Plant.objects.create(name=received_json_data['name'])
        return HttpResponse(received_json_data['name'])

    return HttpResponse('insert success...')
