from django.shortcuts import render
from .models import House
from django.contrib.auth.decorators import login_required
# Create your views here.

def homes(request):
    homes = House.objects.all()
    context = {
        'homes':homes
    }
    return render(request, 'homes/homes.html', context)

@login_required(login_url='/login')
def single_home(request, id):
    home = House.objects.get(id=id)
    homes = House.objects.all()[:3]
    context = {
        'data':home,
        'homes':homes
        
    }
    return render(request, 'homes/singlehome.html', context)