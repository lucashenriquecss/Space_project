from django.contrib import admin
from .models import Gallery
# Register your models here.
from django.contrib.admin.options import ModelAdmin

class GalleryList(admin.ModelAdmin):
    list_display =('id','title','categories','photo','description','date')
    list_display_links= ('id','title')
    search_fields = ('title','date','categories')
    list_per_page = 5

admin.site.register(Gallery, GalleryList)