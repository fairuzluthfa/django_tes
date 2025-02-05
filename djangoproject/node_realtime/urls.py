from django.urls import path
from node_realtime.views import HttpResponse,tes2,bre
# from django.http import HttpResponse

def tes(request):
    print('tes')
    return HttpResponse(f'suksess   ')

urlpatterns = [
    path('<str:pk>',tes2,name='tes'),
    path('bre/',bre,name='bre_link')
]