from django.shortcuts import render
from .models import SodaCombo

# Create your views here.

def filterswig(request):
    soda_object = SodaCombo.objects.all()
    soda_base = request.GET.get('soda')

    # Filters through the soda bases
    if soda_base:
        if soda_base == "drpepper":
            soda_object = base_drpepper(soda_object)
        elif soda_base == "coke":
            soda_object = base_coke(soda_object)
        elif soda_base == "mtndew":
            soda_object = base_mtndew(soda_object)
        elif soda_base == "sprite":
            soda_object = base_sprite(soda_object)
        elif soda_base == "lemonade":
            soda_object = base_lemonade(soda_object)
        elif soda_base == "rootbeer":
            soda_object = base_rootbeer(soda_object)
        elif soda_base == "fresca":
            soda_object = base_fresca(soda_object)

    # Filters through the soda flavors
    soda_flavor = request.GET.get('flavor')

    return render(request, 'sodas/filter.html', {'soda_object': soda_object})

# All the filter functions that filter off of soda base
def base_drpepper(soda_object):
    return soda_object.filter(soda__icontains="Dr. Pepper")

def base_coke(soda_object):
    return (soda_object.filter(soda__icontains="Coca Cola")
            | soda_object.filter(soda__icontains="Diet Coke")
            | soda_object.filter(soda__icontains="Coke Zero"))

def base_mtndew(soda_object):
    return soda_object.filter(soda__icontains="Mountain Dew")

def base_sprite(soda_object):
    return soda_object.filter(soda__icontains="Sprite")

def base_lemonade(soda_object):
    return soda_object.filter(soda__icontains="Lemonade")

def base_rootbeer(soda_object):
    return soda_object.filter(soda__icontains="Root Beer")

def base_fresca(soda_object):
    return soda_object.filter(soda__icontains="Fresca")
