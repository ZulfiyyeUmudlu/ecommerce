from django.db import models
from order.models import WishList
from utils.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='childs',
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='categories',
        null=True,
        blank=True
    )
    is_parent = models.BooleanField(default=False)

    @property
    def product_count(self):
        subcategories = self.childs.all()
        return sum([cat.products.count() for cat in subcategories])

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.FileField(
        upload_to='brands',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class ProductType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product type'
        verbose_name_plural = 'Product types'


class Size(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='sizes',
        on_delete=models.PROTECT,
        null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(BaseModel):
    product_type = models.ForeignKey(
        ProductType,
        related_name='colors',
        on_delete=models.PROTECT,
        null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
    color = models.CharField(max_length=20, null=True)
    size = models.JSONField(null=True)
    siblings = models.ManyToManyField(
        'self',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='products',
        null=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    has_discount = models.BooleanField(default=False)
    old_price = models.DecimalField(
        'əvvəlki qiymət',
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )
    adding_to_basket_count = models.PositiveIntegerField(
        default=0
    )
    # added_to_wish_list = models.BooleanField(default=False)

    # @property
    # def added_to_wish_list(self, user):
    #     try:
    #         wish_list = WishList.objects.get(user=user)
    #         if self in wish_list.product.all():
    #             return True
    #         return False
    #     except WishList.DoesNotExist:
    #         return False
    
    @property
    def added_to_wish_list(self):
        if hasattr(self, '_added_to_wish_list'):
            return self._added_to_wish_list
        return False

    @added_to_wish_list.setter
    def added_to_wish_list(self, value):
        self._added_to_wish_list = value

    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_price = self.price

    def save(self):
        if self.cache_price and self.cache_price != self.price:
            self.has_discount = self.cache_price > self.price
            self.old_price = self.cache_price
        return super().save()
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Comment(BaseModel):
    user = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    text = models.TextField()

    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        default_related_name = 'comments'