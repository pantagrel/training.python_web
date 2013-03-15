from django.http import HttpResponse
from django.shortcuts import render

from plant.models import Plant


def index(request):
    entire_plant_list = Plant.objects.order_by('common_name')
    context = {
        'entire_plant_list': entire_plant_list,
    }
    return render(request, 'plant/index.html', context)
       
def plantDetail(request, plant_id):
    int_id = int(plant_id)
    all_plant_details = Plant.objects.get(id=int_id)
    context = {
        'all_plant_details' : all_plant_details,
    }
    return render(request, 'plant/plantDetail.html', context)
    
def bloomsIndex(request, bloom_time):
    bloomsList = Plant.objects.filter('bloom_time')
    context = {
        'bloomsList': bloomsList,
    }
    return render(request, 'plant/bloomsIndex.html', context) 