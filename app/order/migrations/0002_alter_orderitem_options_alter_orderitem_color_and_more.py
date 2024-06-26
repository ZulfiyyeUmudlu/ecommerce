# Generated by Django 5.0.3 on 2024-05-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0002_remove_product_product_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'default_related_name': 'order_items', 'verbose_name': 'Order item', 'verbose_name_plural': 'Order items'},
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='wish_list', to='product.product'),
        ),
    ]
