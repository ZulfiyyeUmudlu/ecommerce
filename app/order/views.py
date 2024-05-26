from django.shortcuts import render
from .models import Order, OrderItem, WishList


def basket(request):
    items = OrderItem.objects.filter(
        user=request.user,
        status=0
    )
    context = {
        'items': items
    }
    return render(request, 'order/basket.html', context)


def checkout(request):
    order = Order.objects.get(
        user=request.user,
        is_done=False
    )
    context = {
        'order': order
    }
    return render(request, 'order/checkout.html', context)


def wish_list(request):
    wish_list, _ = WishList.objects.get_or_create(user=request.user)
    products = wish_list.product.all()
    context = {
        'wish_list': wish_list,
        'products': products,
    }
    return render(request, 'order/wishlist.html', context)