from django.shortcuts import render

from GalleryApp import models


# Create your views here.
def home(request):
    post = models.Info.objects.all()
    return render(request, 'GalleryApp/index.html', {'form': post})
