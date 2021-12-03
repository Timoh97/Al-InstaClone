from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =300)
    likes = models.CharField(max_length =300)
    comments = models.CharField(max_length =300)
    profile = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    @classmethod
    def search_image(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    bio = models.CharField(max_length =300)
    photo = models.CharField(max_length =300)
    
    def __str__(self):
        return self.name
    
