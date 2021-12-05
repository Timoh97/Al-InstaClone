from django.shortcuts import render, redirect
from .models import *
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

def profile(request):
    current_user = request.user
    # get images for the current logged in user
    images = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'create_profile.html', {"images": images, "profile": profile})
    # return render(request, 'profile.html')
    
def like_image(request, id):
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

def search_images(request):
  if 'search' in request.GET and request.GET['search']:
      search_term = request.GET.get('search').lower()
      images = Image.search_by_image_name(search_term)
      message = f'{search_term}'
      title = message
      return render(request, 'searching.html', {'success': message, 'images': images})

  
def save_image(request):
  if request.method == 'POST':
      image_name = request.POST['image_name']
      image_caption = request.POST['image_caption']
      image_file = request.FILES['image_file']
      image_file = cloudinary.uploader.upload(image_file)
      image_url = image_file['url']
      image_public_id = image_file['public_id']
      image = Image(image_name=image_name, image_caption=image_caption, image=image_url,
                    profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
      image.save_image()
      return redirect('/create_profile', {'success': 'uploading image successfully done'})
      # return render(request, 'profile.html', {'success': 'Image Uploaded Successfully'})
  else:
      return render(request, 'profile.html', {'danger': 'uploading image failed, try again'})
 
 
  else:
      message = 'Search something'
     
      return render(request, 'searching.html', {'danger': message})
