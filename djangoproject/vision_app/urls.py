from django.urls import path,include
from rest_framework.routers import DefaultRouter
from vision_app.views import *
# Nodes_viewset,last_image,upload_image,tes,Login_view,ultg_view

router=DefaultRouter()
router.register(r'devices',Nodes_viewset)

urlpatterns=[
    path('',include(router.urls)),
    path('image/<str:pk>/',last_image),
    path('upload_image/<str:id>/',upload_image),
    path('test/',tes),
    path('login/',Login_view),
    path('upt/',upt_view),
    path('ultg/',ultg_view),
    path('gi/',gi_view)
]