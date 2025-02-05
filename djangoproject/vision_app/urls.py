from django.urls import path,include
from rest_framework.routers import DefaultRouter
from vision_app.views import Nodes_viewset

router=DefaultRouter()
router.register(r'devices',Nodes_viewset)

urlpatterns=[
    path('',include(router.urls))
]