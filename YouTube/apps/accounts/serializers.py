from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    CharField,
    ValidationError,
    )

from .models import MyUser, Channel

class MyUserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'profile_picture', 'bio','password','confirm_password']

    def validate(self, data):
        if MyUser.objects.filter(username=data.get('username')).exists():
            raise ValidationError({"username": "Username already exists!"})
        
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError({"password": "Password do not match!"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  
        return MyUser.objects.create_user(**validated_data)
    
    
    
class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True, min_length=8)
    confirm_password = CharField(required=True, min_length=8)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise ValidationError({"error": "New passwords do not match"})
        return data


class ChannelCreateUpdateSerializer(ModelSerializer):
    owner = MyUserSerializer(read_only=True)
    class Meta:
        model = Channel
        fields = ['name', 'owner','description', 'image', 'banner','created_at','updated_at']
        
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['owner'] = user
        return Channel.objects.create(**validated_data)
        
        
        
from apps.content.models import Category
from apps.content.serializers import CategorySerializer, VideoSerializer
class ChannelRetrieveSerializer(ModelSerializer):
    subscribers_count = SerializerMethodField()
    categories = SerializerMethodField()
    videos_count = SerializerMethodField()
    videos_list = SerializerMethodField()
    
    class Meta:
        model = Channel
        fields = ['name', 'owner','description', 'image', 'banner','subscribers_count','categories','videos_count','videos_list']
        
    def get_subscribers_count(self, obj):
        return obj.subscribers.count()
    
    def get_categories(self, obj):
        categories = Category.objects.all().order_by('name')
        return CategorySerializer(categories, many=True).data
    
    def get_videos_list(self, obj):
        default_category =  Category.objects.all().order_by('name').first()
        category = self.context.get('request').query_params.get('slug').capitalize()
        if category:
            try:
                category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                category = default_category
        else:
            category = default_category
        videos = obj.videos.filter(category=category)
        return VideoSerializer(videos, many=True).data
    
    def get_videos_count(self, obj):
        return obj.videos.count()
        

class ChannelListSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = ['name', 'image']  
        

    