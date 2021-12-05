from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
#setting cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.


def index(request):
    # get all the images from the database and order them by the date they were created
    images = Image.objects.all().order_by('-image_date')
    return render(request, 'index.html', {'images': images})

