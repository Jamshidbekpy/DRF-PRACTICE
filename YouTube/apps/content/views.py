from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category
from .serializers import CategorySerializer
# Create your views here.


class CategoryListAPIView(ListAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer