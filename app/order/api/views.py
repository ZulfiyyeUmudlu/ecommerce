import json
from rest_framework import generics
from rest_framework.response import Response

from product.models import Product

from ..models import Order, OrderItem, WishList
from .serializers import (OrderCreateSerializer,
                          OrderIsDoneSerializer,
                          OrderItemSerializer,
                          OrderItemDeleteSerializer,
                          AddProductToWishListSerializer
                        )


class OrderItemCreateAPIView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_item = OrderItem.objects.filter(
            product=serializer.validated_data.get('product'),
            user=request.user,
            status=0,
            size=serializer.validated_data.get('size')
        ).first()

        if order_item:
            order_item.quantity += serializer.validated_data.get('quantity')
            order_item.product.adding_to_basket_count += 1
            order_item.save()
        else:
            instance = serializer.save()
            instance.user = request.user
            instance.save()
            # increasing count of adding product to basket
            instance.product.adding_to_basket_count += 1
            instance.product.save()
        data = serializer.data
        return Response(data={"detail": "OK", 'data': data}, status=201)


class OrderItemDeleteApiView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemDeleteSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order.user = request.user
        order.save()

        Order.objects.filter(user=request.user, is_done=False).exclude(id=order.id).delete()
        item_ids = json.loads(request.data.get('items', '[]'))
        for item in item_ids:
            order_item = OrderItem.objects.get(id=item['id'])
            order_item.order = order
            order_item.quantity = item['quantity']
            order_item.save()

        data = serializer.data
        return Response(data={"detail": "OK", 'data': data}, status=201)


class OrderIsDoneAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderIsDoneSerializer

    def put(self, request, *args, **kwargs):
        order = self.get_object()
        order.is_done = True
        order.save()
        for item in order.items.all():
            item.status = 1
            item.save()
        return Response(data={"detail": "OK"}, status=200)


class AddProductToWishListAPIView(generics.CreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = AddProductToWishListSerializer

    def post(self, request, *args, **kwargs):
        wish_list, _ = WishList.objects.get_or_create(user=request.user)
        product_id = json.loads(request.data.get('product', '[]'))
        print('product_id', product_id)
        product = Product.objects.get(id=product_id[0])
        wish_list.product.add(product)
        return Response(data={"detail": "OK"}, status=200)


class RemoveProductToWishListAPIView(generics.CreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = AddProductToWishListSerializer

    def post(self, request, *args, **kwargs):
        wish_list, _ = WishList.objects.get_or_create(user=request.user)
        product_id = json.loads(request.data.get('product', '[]'))
        print('product_id', product_id)
        product = Product.objects.get(id=product_id[0])
        wish_list.product.remove(product)
        return Response(data={"detail": "OK"}, status=200)