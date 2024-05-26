from rest_framework import serializers
from ..models import OrderItem, Order, WishList


class OrderItemSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderItem
        fields = ['product', 'size', 'color', 'quantity']


class OrderItemDeleteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = ['id']


class OrderCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = ['subtotal', 'total', 'shipping']


class OrderIsDoneSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = ['is_done']


class AddProductToWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['product']