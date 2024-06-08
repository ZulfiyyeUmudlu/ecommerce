from typing import Any

from django.db.models import Q
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView
from order.models import WishList

from .models import Product

# def products(request): # function based product list view
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'product/list.html', context)

class ProductListView(ListView):
    template_name = "product/list.html"
    model = Product
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset()
        if 'filter' in self.request.GET:
            our_filter = self.request.GET['filter']
            if our_filter == 'latest':
                qs = qs.order_by('-created_at')
            elif our_filter == 'trandy':
                qs = qs.order_by('-adding_to_basket_count')
            elif our_filter == 'increased_price':
                qs = qs.order_by('price')
            elif our_filter == 'decreased_price':
                qs = qs.order_by('-price')
        if 'start_price' in self.request.GET and 'end_price' in self.request.GET:
            start_price = self.request.GET.get('start_price')
            end_price = self.request.GET.get('end_price')

            start_price = int(start_price) if start_price else 0
            end_price = int(end_price) if end_price else 10000
            qs = qs.filter(price__range=[start_price, end_price])
            if self.request.user.is_authenticated:
             qs = is_in_wish_list(qs, self.request.user)
        return qs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if 'start_price' in self.request.GET and 'end_price' in self.request.GET:
            start_price = self.request.GET.get('start_price')
            end_price = self.request.GET.get('end_price')
            
            start_price = int(start_price) if start_price else 0
            end_price = int(end_price) if end_price else 10000
            context['start_price'] = start_price
            context['end_price'] = end_price
        if 'filter' in self.request.GET:
            our_filter = self.request.GET['filter']
            if our_filter == 'latest':
                context['our_filter'] = _('Latest')
            elif our_filter == 'trandy':
                context['our_filter'] = _('Popularity')
            elif our_filter == 'increased_price':
                context['our_filter'] = _('Increased price')
            elif our_filter == 'decreased_price':
                context['our_filter'] = _('Decreased price')
        else:
            context['our_filter'] = _('Sort by')
            
        context['products'] = is_in_wish_list(context['products'], self.request.user)
        return context


def is_in_wish_list(products, user):
    for product in products:
        try:
            wish_list = WishList.objects.get(user=user)
            if product in wish_list.product.all():
                product.added_to_wish_list = True
            else:
                product.added_to_wish_list = False
        except WishList.DoesNotExist:
            product.added_to_wish_list = False
    return products

    

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        sizes = [size for size in self.get_object().size]
        context['sizes'] = sizes

        return context


def search(request):
    search_input = request.GET.get('search_input')
    result = []
    if search_input:
        result = Product.objects.filter(Q(name__icontains=search_input) | Q(description__icontains=search_input))
    context = {
        'results': result,
        'result_count': len(result),
        'keyword': search_input
    }
    return render(request, 'search.html', context)