from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('products/index.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))

def new_product(request):
    template = loader.get_template('products/new.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))


def add_new_product(request):
    template = loader.get_template('products/new.html')

    pk=request.POST['title']
    context = {
        pk: "Hello, World"
    }
    return HttpResponse(template.render(context, request))
