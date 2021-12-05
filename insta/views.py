from django.shortcuts import render, redirect
from .models import *
from django.http  import HttpResponse

# Create your views here.


def index(request):
    # get all the images from the database and order them by the date they were created
    images = Image.objects.all().order_by('-image_date')
    return render(request, 'index.html', {'images': images})

def profile(request):
    current_user = request.user
    # get images for the current logged in user
    images = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})
    # return render(request, 'profile.html')
    
ef like_image(request, id):
   likes = Likes.objects.filter(image_id=id).first()
   # check if the user has already liked the image
   if Likes.objects.filter(image_id=id, user_id=request.user.id).exists():
       # unlike the image
       likes.delete()
       # reduce the number of likes by 1 for the image
       image = Image.objects.get(id=id)
       # check if the image like_count is equal to 0
       if image.like_count == 0:
           image.like_count = 0
           image.save()
       else:
           image.like_count -= 1
           image.save()
       return redirect('/')
   else:
       likes = Likes(image_id=id, user_id=request.user.id)
       likes.save()
       # increase the number of likes by 1 for the image
       image = Image.objects.get(id=id)
       image.like_count = image.like_count + 1
       image.save()
       return redirect('/')

  

