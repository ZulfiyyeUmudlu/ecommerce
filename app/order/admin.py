from django.contrib import admin
from .models import Order, OrderItem, WishList


admin.site.register(WishList)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_full_name', 'get_user_email', 'shipping', 'total', 'is_done', 'created_at')
    inlines = [OrderItemAdmin]

    def get_user_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_user_email(self, obj):
        return obj.user.email
    
    get_user_full_name.short_description = 'Ad Soyad'
    get_user_email.short_description = 'E-poçt'