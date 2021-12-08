from django.http import request, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Image, Profile, Like, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html', {"images":images})

# Display the details of an image
@login_required(login_url='/accounts/login/')
def image_detail(request, photo_id):
  try:
    image_details = Image.objects.get(pk = photo_id)
    image_comments = Comment.objects.filter(image_id= photo_id).all()
  except DoesNotExist:
    raise Http404

  if request.method == "POST":
    form = CommentForm(request.POST)
    image = image_details
    if form.is_valid():
      comment_message = form.cleaned_data.get('comment_message')
      form.instance.user = request.user
      form.instance.image = image
      form.save()
      return redirect('home')
  else:
    form = CommentForm()
  return render(request, "detailedImage.html", {"details":image_details, "form":form, "comments":image_comments})

# profile page
@login_required(login_url='/accounts/login/')
def profile(request):
  current_user = request.user.id
  images = Image.objects.filter(user_id = current_user)
  return render(request, 'profile.html', {"images":images})

@login_required(login_url='/accounts/login/')
def post_image(request):
  current_user=request.user
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    profile = Profile.objects.get()
    if form.is_valid():
      image = form.save(commit=False)
      image_name = form.cleaned_data.get('image_name')
      image_caption = form.cleaned_data.get('image_caption')
      form.instance.profile = profile
      form.instance.user = request.user
      
      form.save()
      return redirect('home')
  else:
    form = ImageForm()
    
  return render(request, "newpost.html", {"form":form})