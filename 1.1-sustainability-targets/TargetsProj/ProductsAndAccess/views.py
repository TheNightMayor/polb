from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Route, Product


class IndexView(generic.ListView):
    template_name = "ProductsAndAccess/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        """
        Return the last five published products (not including those set to be
        published in the future).
        """
        return Product.objects.order_by("-id")[
            :5
    ]

class DetailView(generic.DetailView):
    model = Product
    template_name = "ProductsAndAccess/detail.html"
    """
    Excludes any products that aren't published yet.
    """
        

def index(request):
    product_list = Product.objects.order_by("-id")[:5]
    context = {"product_list": product_list}
    return render(request, "ProductsAndAccess/index.html", context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "ProductsAndAccess/detail.html", {"Product": product})


def results(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "ProductsAndAccess/results.html", {"Product": product})

# Create your views here.
