from django.contrib import admin

from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Product, ProductAdmin)