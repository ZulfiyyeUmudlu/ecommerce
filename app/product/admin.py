from django.contrib import admin
from .models import Comment, Product, ProductType, Color, Size, Category, Brand
from .forms import CategoryAdminForm

admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm