from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_product, name='new_product'),
    path('add_new_product', views.new_product, name='add_new_product'),
    path('<int:pk>', views.product_preview, name='product_preview'),
]
    