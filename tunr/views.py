from django.shortcuts import render

from django.shortcuts import render

from .models import Artist, Song

def artist_index(request):
    context = {'artists': Artist.objects.all()}
    return render(request, 'tunr/artist_index.html', context)

def song_list(request):
    context = {'songs': Song.objects.all()}
    return render(request, 'tunr/song_list.html', context)