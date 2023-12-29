from django.contrib import admin
from pages.models import *


@admin.register(CategoryModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductsModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(BookingModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ImagesModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name']
