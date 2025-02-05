from django.urls import path,include
from django.http import HttpResponse
from myapp.views import ItemViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'items',ItemViewSet)
# def tes(request):
#     print('1')
#     return HttpResponse('tes')

urlpatterns=[
    path('',include(router.urls)),
             ]