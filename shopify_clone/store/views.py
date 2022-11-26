from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('store/index.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))

def orders(request):
    template = loader.get_template('orders/index.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))

def products(request):
    template = loader.get_template('products/index.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))


def customers(request):
    template = loader.get_template('customers/index.html')

    message = "Hello, World"
    context = {
        message: "Hello, World"
    }
    return HttpResponse(template.render(context, request))