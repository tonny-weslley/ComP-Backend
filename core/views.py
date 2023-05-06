from django.shortcuts import render
from rest_framework import viewsets

from .models import Category, Product, Register, Store, User, Variation
from .serializers import (CategorySerializer, ProductSerializer,
                          RegisterSerializer, StoreSerializer, UserSerializer,
                          VariationSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
