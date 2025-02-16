from django.contrib import admin
from .models import Category,Video
# Register your models here.

admin.site.register(Category)
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','category','channel')
    

