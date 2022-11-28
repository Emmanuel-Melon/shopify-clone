from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect
from .models import Product

# Create your views here.


def index(request):
    template = loader.get_template('products/index.html')

    products = Product.objects.all()
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))


def new_product(request):
    template = loader.get_template('products/new.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))


def product_preview(request, pk):
    template = loader.get_template('products/product_preview.html')
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))


def add_new_product(request):
    template = loader.get_template('products/new.html')

    pk = request.POST['title']
    context = {
        pk: "Hello, World"
    }
    return HttpResponse(template.render(context, request))
