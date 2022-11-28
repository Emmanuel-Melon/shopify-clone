from django.contrib import admin

from . import models

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Order, OrdersAdmin)