from django.urls import path
from image_app.views import upload_image,image_list
from django.http import HttpResponse

def tes(request):
    return HttpResponse('ok')

urlpatterns=[
    path('upload/',upload_image,name='upload_image'),
    path('images/',image_list,name='image_list')
]


