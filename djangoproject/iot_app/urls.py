from django.urls import path,include
from rest_framework.routers import DefaultRouter
from iot_app.views import DeviceViewSet,unique

router=DefaultRouter()
router.register(r'devices',DeviceViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('unique/',unique)
]