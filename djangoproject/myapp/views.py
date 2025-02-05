from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Item
from myapp.serializer import ItemSerializer
# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    # queryset=Item.objects.all()
    # queryset=Item.objects.get(description='nuvo')
    queryset=Item.objects.filter(name='sabun')
    serializer_class=ItemSerializer