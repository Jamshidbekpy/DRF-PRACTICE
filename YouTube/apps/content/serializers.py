from rest_framework.serializers import ModelSerializer
from .models import Category, Video

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'description', 'photo', 'category')

        