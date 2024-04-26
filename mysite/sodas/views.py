from django.shortcuts import render
from .models import SodaCombo

# Create your views here.

def filterswig(request):
    soda_object = SodaCombo.objects.all()
    soda_base = request.GET.get('soda')

    if soda_base:
        if soda_base == "drpepper":
            soda_object = filter_drpepper(soda_object)
        elif soda_base == "coke":
            soda_object = filter_coke(soda_object)
        elif soda_base == "mtndew":
            soda_object = filter_mtndew(soda_object)
        elif soda_base == "sprite":
            soda_object = filter_sprite(soda_object)
        elif soda_base == "lemonade":
            soda_object = filter_lemonade(soda_object)
        elif soda_base == "rootbeer":
            soda_object = filter_rootbeer(soda_object)
        elif soda_base == "fresca":
            soda_object = filter_fresca(soda_object)

    return render(request, 'sodas/filter.html', {'soda_object': soda_object})

# All the filter functions that filter off of soda base
def filter_drpepper(soda_object):
    return soda_object.filter(soda__icontains="Dr. Pepper")

def filter_coke(soda_object):
    return (soda_object.filter(soda__icontains="Coca Cola")
            | soda_object.filter(soda__icontains="Diet Coke")
            | soda_object.filter(soda__icontains="Coke Zero"))

def filter_mtndew(soda_object):
    return soda_object.filter(soda__icontains="Mountain Dew")

def filter_sprite(soda_object):
    return soda_object.filter(soda__icontains="Sprite")

def filter_lemonade(soda_object):
    return soda_object.filter(soda__icontains="Lemonade")

def filter_rootbeer(soda_object):
    return soda_object.filter(soda__icontains="Root Beer")

def filter_fresca(soda_object):
    return soda_object.filter(soda__icontains="Fresca")
