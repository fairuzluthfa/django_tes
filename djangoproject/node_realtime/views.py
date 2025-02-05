from django.shortcuts import render
from django.http import HttpResponse
from .models import realtime_data

def tes2(request,pk):
    print('tes2')
    return HttpResponse(f'tes22 ok {pk}')

def bre(request):
    data=realtime_data()
    
    return HttpResponse('bre')


# Create your views here.
