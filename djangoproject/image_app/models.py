from django.db import models
import os

# Create your models here.

class ImageUpload(models.Model):
    image=models.ImageField(upload_to='images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
    # Delete the file from the filesystem before deleting the database entry
        if self.image:
            image_path = self.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)