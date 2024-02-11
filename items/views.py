from django.shortcuts import render, HttpResponse, redirect
from .models import *

def home(request):
   return HttpResponse("you are on home")

def Item(request):
   item_objs = Items.objects.all()
   print(item_objs)
   return render(request , "items.html" , {'item_objs' : item_objs})


# Create your views here.
