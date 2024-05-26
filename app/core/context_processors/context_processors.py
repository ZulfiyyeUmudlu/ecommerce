from order.models import OrderItem, WishList
from contact.models import ContactInfo
from product.models import Category


def subject_renderer(request):
    context = {
        'contact_info': ContactInfo.objects.first(),
        'categories': Category.objects.filter(parent__isnull=True)
    }

    if request.user.is_authenticated:
        context.update({
            'basket_order_count': OrderItem.objects.filter(user=request.user, status=0).count() or 0,
            'wish_list_count': WishList.objects.filter(user=request.user).first().product.count() if WishList.objects.filter(user=request.user).first() else 0
            })
    return context