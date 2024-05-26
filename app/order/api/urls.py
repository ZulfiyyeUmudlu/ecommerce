from django.urls import path

from . import views

urlpatterns = [
    path('order-create', views.OrderCreateAPIView.as_view(), name='order_create'),
    path('order-item-create', views.OrderItemCreateAPIView.as_view(), name='order_item_create'),
    path('order-item-delete/<int:pk>', views.OrderItemDeleteApiView.as_view(), name='order_item_delete'),
    path('order-item-is-done/<int:pk>', views.OrderIsDoneAPIView.as_view(), name='order_item_is_done'),
    path('add-product-to-wish-list', views.AddProductToWishListAPIView.as_view(), name='add_to_wish_list'),
    path('remove-product-to-wish-list', views.RemoveProductToWishListAPIView.as_view(), name='remove_to_wish_list'),
]