from django.shortcuts import render

from product.models import Category


def index(request):
    categories = Category.objects.filter(is_parent=True)
    context = {
        'categories' : categories
        
    }
    return render(request, 'home/index.html',context)