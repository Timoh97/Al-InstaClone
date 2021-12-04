from django.db import models

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    def __str__(self):
        return self.