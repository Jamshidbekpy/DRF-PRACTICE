from django.db import models
from django.utils.text import slugify
from apps.base.models import BaseModel

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)  

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name
    
# from apps.accounts.models import Channel
class Video(BaseModel):
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='video_photos/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='videos')
    channel = models.ForeignKey('accounts.Channel', on_delete=models.CASCADE,related_name='videos')
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
