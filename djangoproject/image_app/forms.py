from django import forms
from image_app.models import ImageUpload

class ImageUpload_Form(forms.ModelForm):
    class Meta:
        model=ImageUpload
        fields=['image']