from django.contrib import admin

from . import models

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Store, StoreAdmin)