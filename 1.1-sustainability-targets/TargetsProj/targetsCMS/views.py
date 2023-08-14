from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Sequence, Playlist


class IndexView(generic.ListView):
    template_name = "targetsCMS/index.html"
    context_object_name = "playlist_list"

    def get_queryset(self):
        """
        Return the last five published playlists (not including those set to be
        published in the future).
        """
        return Playlist.objects.order_by("-id")[
            :5
    ]

class DetailView(generic.DetailView):
    model = Playlist
    template_name = "targetsCMS/detail.html"
    """
    Excludes any playlists that aren't published yet.
    """


def index(request):
    playlist_list = Playlist.objects.order_by("-id")[:5]
    context = {"playlist_list": playlist_list}
    return render(request, "targetsCMS/index.html", context)


def detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, "targetsCMS/detail.html", {"playlist": playlist})


def results(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, "targetsCMS/results.html", {"playlist": playlist})

# Create your views here.
