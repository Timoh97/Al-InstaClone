from django import forms
from .models import Image, Profile, Comment

class CommentForm(forms.ModelForm):
  comment_message = forms.CharField(widget=forms.Textarea(attrs={
    'rows':'3',
  }))
  class Meta:
    model = Comment
    exclude = ('posted_on', 'user', 'image')
    
class ImageForm(forms.ModelForm):
  image = forms.ImageField()
  image_name = forms.CharField(max_length=30)
  image_caption = forms.CharField(widget=forms.Textarea(attrs={
    'rows':'3',
  }))
  
  class Meta:
    model = Image
    exclude = ('profile', 'user', 'date_posted')
    