from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    CurrentUserDefault,
    HiddenField,
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

class ChannelCreateSerializer(ModelSerializer):
    owner = MyUserSerializer(read_only=True)
    class Meta:
        model = Channel
        fields = ['name', 'owner','description', 'image', 'banner','created_at','updated_at']
        
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['owner'] = user
        return Channel.objects.create(**validated_data)
        
        