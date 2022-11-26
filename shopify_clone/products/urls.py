from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/new', views.new_product, name='new_product'),
]
    