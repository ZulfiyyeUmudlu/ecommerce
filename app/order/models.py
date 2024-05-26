from django.db import models
from utils.models import BaseModel
from utils.options import ORDER_STATUSES


class Order(BaseModel):
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    shipping = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(
        'account.Account',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user.email} - {self.total}"


class WishList(BaseModel):
    user = models.ForeignKey(
        'account.Account',
        related_name='wish_list',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        'product.Product',
        related_name='wish_list',
        blank=True
    )

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish list'

    def __str__(self):
        return f"{self.user.email}"


class OrderItem(BaseModel):
    user = models.ForeignKey(
        'account.Account',
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
    )
    size = models.CharField(max_length=20, null=True)   
    color = models.CharField(max_length=20, null=True)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        'order.Order', 
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        choices=ORDER_STATUSES,
        default=0
    )

    def __str__(self) -> str:
        return self.product.name
    
    @property
    def get_total_price(self):
        return self.quantity * self.product.price # type: ignore
    
    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
        default_related_name = 'order_items'