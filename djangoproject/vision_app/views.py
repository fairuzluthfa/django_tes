from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from vision_app.models import nodes_model,realtimes_model
from vision_app.serializer import nodes_serializer,realtimes_serializer
from datetime import datetime

# Create your views here.


class Nodes_viewset(viewsets.ModelViewSet):
    queryset=nodes_model.objects.all()
    serializer_class=nodes_serializer
    