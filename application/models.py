from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  profile_photo= CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  # save profile method
  def save_profile(self):
    self.save()
    
  # Save profile method
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.bio

class Image(models.Model):
  image = models.CloudinaryField('image')
  image_name = models.CharField(max_length=30)
  image_caption = models.TextField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(auto_now=True)
  
  # Save image method
  def save_image(self):
    self.save()
    
  # Get all images method
  @classmethod
  def get_all_images(cls):
    all_images=cls.objects.all()
    return all_images
  
  def __str__(self):
    return self.image_name
  
class Like(models.Model):
  like=models.IntegerField()
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.like
  
  
class Comment(models.Model):
  comment_message = models.TextField()
  posted_on = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username