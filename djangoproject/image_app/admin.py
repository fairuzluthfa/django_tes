from django.contrib import admin
from image_app.models import ImageUpload
import os


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')

    def delete_model(self, request, obj):
        """Delete image file from media before deleting database entry."""
        if obj.image:
            image_path = obj.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        print('deleteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeed')
        super().delete_model(request, obj)

# Register your models here.
admin.site.register(ImageUpload)