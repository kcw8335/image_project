from django.shortcuts import render
from .models import Media

def media(request):
    medias = Media.objects
    context = { 'medias' : medias }
    return render(request, 'media.html', context)