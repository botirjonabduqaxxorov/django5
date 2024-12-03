# from django.shortcuts import render

from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

# Create your views here.
