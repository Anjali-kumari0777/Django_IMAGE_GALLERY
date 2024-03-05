from django.contrib import admin
from .models import Imagemodel


@admin.register(Imagemodel)
class ImagemodelAdmin(admin.ModelAdmin):
    list_display=['id','date','image']
