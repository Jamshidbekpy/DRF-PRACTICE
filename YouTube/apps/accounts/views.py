from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import MyUserSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.

from .models import MyUser,Channel
class RegisterView(CreateAPIView):
    permission_classes = []
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
    
    
from rest_framework_simplejwt.tokens import RefreshToken
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ShowProfile(APIView):
    def get(self, request):
        user = request.user
        serializer = MyUserSerializer(user)
        return Response(serializer.data)
    
# class ChangePasswordView(APIView):
#     def post(self, request):
#         user = request.user
#         new_password = request.data.get('new_password')
#         user.set_password(new_password)
#         user.save()
#         return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)

from .serializers import ChannelCreateSerializer
class ChannelCreateAPIView(CreateAPIView):
    serializer_class = ChannelCreateSerializer
    queryset = Channel.objects.all()
    
