from rest_framework import routers, serializers, viewsets

from .models import Category, Product, Register, Store, User, Variation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'cover_image', 'joined_in']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'color']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description',
                  'cover_image', 'category', 'created_at']


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['id', 'name', 'product', 'created_at']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'address',
                  'phone', 'email', 'logo', 'cover_image']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'store', 'product', 'variation',
                  'last_price', 'price', 'created_at', 'last_editor', 'edit_at']
