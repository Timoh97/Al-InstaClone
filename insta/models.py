from django.db import models

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.image.namespace
    
class Profile(models.Model):
    bio = models.TextField(max_length=300, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    contact = models.CharField(max_length=30, blank=True, null=True)
    
        def save_the_profile(self):
        self.save()
        
        def __str__(self):
        return self.user.username
class Comments(models.Model):
     image = models.ForeignKey(Image, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     comment_date = models.DateTimeField(auto_now_add=True)
     comment = models.CharField(max_length=150)
     
     
      def save_the_comment(self):
        self.save()
        
        
    def __str__(self):
        return self.comment
    
class Likes(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.