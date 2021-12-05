from django.shortcuts import render, redirect
from .models import *
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to instaclone')
