from django.http import HttpResponse
from django.shortcuts import render

from plant.models import Plant


def index(request):
    entire_plant_list = Plant.objects.order_by('common_name')
#     plant_images = Plant.objects.filter('plant_image')
    context = {
        'entire_plant_list': entire_plant_list,
#         'plant_images': plant_images,
    }
    return render(request, 'plant/index.html', context)
       
def plantDetail(request, plant_id):
    int_id = int(plant_id)
    all_plant_details = Plant.objects.get(id=int_id)
    context = {
        'all_plant_details' : all_plant_details,
    }
    return render(request, 'plant/plantDetail.html', context)

def subIndex(request, pk='Zilch'):
#     can I make dictionaries populate from the database? please?
    bloomTimeD = {'Spring': 'Spring', 'Summer':'Summer', 'Fall':'Fall', 'Winter': 'Winter',}
    plantTypeD = {'Shrub': 'Shrub', 'Vine':'Vine', 'Tree':'Tree', 'Conifer':'Conifer',}
    sunNeedsD = {'full-sun': 'Full Sun', 'part-sun':'Part Sun', 'shade': 'Shade',}
    if pk in bloomTimeD:
        list_of_stuff = Plant.objects.filter(bloom_time=pk).order_by('common_name')
#         for 'other_stuff' list::::
#         build a dictionary: 'sun_need': ['item', 'item', 'item', 'item',],
        other_stuff = Plant.objects.exclude(bloom_time=pk).order_by('common_name')
        pageHeader = ('Plants that bloom in %s:' % pk)
    elif pk in plantTypeD:
        list_of_stuff = Plant.objects.filter(plantType=pk).order_by('common_name')
        other_stuff = 'monkeybanana'
        pageHeader = ('%s-type plants:' % pk)
    elif pk in sunNeedsD:
        sunLabel = sunNeedsD[pk]
        list_of_stuff = Plant.objects.filter(sun_needs=sunLabel).order_by('common_name')
        other_stuff = 'monkeyfuck'
        pageHeader = ('Plants that need %s:' % sunLabel)
    context = {
        'list_of_stuff': list_of_stuff,
        'pk' : pk,
        'pageHeader': pageHeader,
        'other_stuff': other_stuff,
    }
    return render(request, 'plant/subIndex.html', context)
