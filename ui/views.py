from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def upload(request):
    return render(request,'video/upload.html')


def stream(request):
    return render(request,'video/stream.html')


