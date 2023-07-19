from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Sequence, Playlist


class IndexView(generic.ListView):
    template_name = "dataViz/index.html"
    context_object_name = "latest_playlist_list"

    def get_queryset(self):
        """
        Return the last five published playlists (not including those set to be
        published in the future).
        """
        return Playlist.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
    ]

class DetailView(generic.DetailView):
    model = Playlist
    template_name = "dataViz/detail.html"
    def get_queryset(self):
        """
        Excludes any playlists that aren't published yet.
        """
        return Playlist.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Playlist
    template_name = "dataViz/results.html"


def index(request):
    latest_playlist_list = Playlist.objects.order_by("-pub_date")[:5]
    context = {"latest_playlist_list": latest_playlist_list}
    return render(request, "dataViz/index.html", context)


def detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, "dataViz/detail.html", {"playlist": playlist})


def results(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, "dataViz/results.html", {"playlist": playlist})


def vote(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    try:
        selected_sequence = playlist.sequence_set.get(pk=request.POST["sequence"])
    except (KeyError, Sequence.DoesNotExist):
        # Redisplay the playlist form.
        return render(
            request,
            "dataViz/detail.html",
            {
                "playlist": playlist,
                "error_message": "You didn't select a sequence.",
            },
        )
    else:
        selected_sequence.votes += 1
        selected_sequence.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("dataViz:results", args=(playlist.id,)))

# Create your views here.
