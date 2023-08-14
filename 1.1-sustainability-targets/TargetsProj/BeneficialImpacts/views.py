from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Topic, Story, Content


class IndexView(generic.ListView):
    template_name = "BeneficialImpacts/index.html"
    context_object_name = "content_list"

    def get_queryset(self):
        """
        Return the last five published products (not including those set to be
        published in the future).
        """
        return Content.objects.order_by("-id")[
            :5
    ]

class DetailView(generic.DetailView):
    model = Content
    template_name = "BeneficialImpacts/detail.html"
    """
    Excludes any products that aren't published yet.
    """
        

def index(request):
    content_list = Content.objects.order_by("-id")[:5]
    context = {"content_list": content_list}
    return render(request, "BeneficialImpacts/index.html", context)


def detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, "BeneficialImpacts/detail.html", {"Content": content})


def results(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    return render(request, "BeneficialImpacts/results.html", {"Content": content})

# Create your views here.
