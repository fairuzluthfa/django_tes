from django.contrib import admin
from vision_app.models import nodes_model,realtimes_model

# Register your models here.
admin.site.register(nodes_model)
admin.site.register(realtimes_model)