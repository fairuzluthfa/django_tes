from django.shortcuts import render,redirect
from image_app.forms import ImageUpload_Form
from image_app.models import ImageUpload

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

def image_list(request):
    images=ImageUpload.objects.all()
    return render(request,'image_list.html',{'images':images})