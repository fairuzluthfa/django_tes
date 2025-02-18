from django.shortcuts import render,redirect
from image_app.forms import ImageUpload_Form
from image_app.models import ImageUpload
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from image_app.serializers import image_serializer
from rest_framework.response import Response
# Create your views here.
def upload_image(request):
    print('deleteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeed aja')
    if request.method=='POST':
        form=ImageUpload_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')    # Redirect to a page showing uploaded images
    else:
        form=ImageUpload_Form()
    return render(request,'upload.html',{'form':form})

@api_view(['GET'])
def image_list(request):
    images=ImageUpload.objects.all()
    serializer=image_serializer(images,many=True)
    return Response(serializer.data)
    # for image in images:
    #     print(request.build_absolute_uri(image.image.url))
    # return render(request,'image_list.html',{'images':images})






@api_view(['DELETE'])
def delete_all(request):
    """
    Delete all image files from the media folder
    """
    try:
        ImageUpload.objects.all().delete()
        # List of common image extensions
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
        deleted_files = []
        
        # Walk through all directories in media folder
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for file in files:
                if file.lower().endswith(image_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        # Get relative path for reporting
                        rel_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
                        deleted_files.append(rel_path)
                    except Exception as e:
                        print(f"Error deleting {file}: {str(e)}")
        
        if deleted_files:
            return Response({
                'message': f'Successfully deleted {len(deleted_files)} images',
                'deleted_files': deleted_files
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'No image files found in media directory'
            }, status=status.HTTP_200_OK)
            
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)