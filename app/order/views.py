from django.shortcuts import render
from product.views import is_in_wish_list

# from order.tasks import send_sms_when_status_changed

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
    result = is_in_wish_list(products, request.user)

    context = {
        'wish_list': wish_list,
        'products': result,
    }
    return render(request, 'order/wishlist.html', context)

