from django.shortcuts import render,HttpResponse,redirect
import zipcode
from django.contrib.auth.models import User
from ..users.models import Profile
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login

def index(request):
    user=request.user
    return render(request,'home/home.html',{'user':user})



def loc(request,lon,lat):
    print lon
    print lat

    myzip = zipcode.coordinate(round(float(lon),2),round(float(lat),2))
    myzip2 = zipcode.coordinate(-122.41,37.79)
    print myzip2.city
    return HttpResponse(str(myzip.city))