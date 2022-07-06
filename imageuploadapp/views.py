from django.shortcuts import render
from django.http import HttpResponse
from imageuploadapp.forms import ImageUploadForm
from imageuploadapp.models import ImageUplaodModel

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Image Uploaded successfully</h2>')
    else:
        form = ImageUploadForm()
        images = ImageUplaodModel.objects.all()
    return render(request,'imageupload.html',{'form':form,'images':images})

