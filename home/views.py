from django.shortcuts import render
from homes.models import House
from .models import Team
from django.db.models import Q
# Create your views here.
def home(request):
    homes = House.objects.all()
    team = Team.objects.all()

    qs = request.GET.get('q')
    if qs:
        homes = House.objects.filter(
            Q(title__icontains=qs)|
            Q(rent__icontains=qs)|
            Q(bedroom_range=qs)|
            Q(bathroom__icontains=qs)|
            Q(area__icontains=qs)|
            Q(house_type__icontains=qs)|
            Q(location__icontains=qs)|
            Q(kitchen__icontains=qs)).order_by('-id')
    context = {
        'homes':homes,
        'team':team
    }
    return render(request,'home/home.html', context)


def about(request):
    homes = House.objects.all()
    team = Team.objects.all()
    context = {
        'homes':homes,
        'team':team
    }
    return render(request, 'home/about.html', context)


def ourApp(request):
    return render(request, 'home/comingsoon.html')





#0689810880      0652404583