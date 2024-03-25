from django.db import models
from users.models import CustomUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Seller(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=500)


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()


class Promocode(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    is_active = models.BooleanField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    description = models.TextField()
    count_on_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(Seller, null=True, blank=True, on_delete=models.CASCADE)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class Order(models.Model):
    STATUS = (
        ('in Process', 'In Process'),
        ('Packed', 'Packed'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Received', 'Received'),
        ('Refused', 'Refused')
    )
    DELIVERY_METHODS = (
        ('Courier', 'Courier'),
        ('Post', 'Post'),
        ('Self-delivery', 'Self delivery')
    )
    PAYMENT_METHOD = (
        ('Card Online', 'Card Online'),
        ('Card Offline', 'Card Offline'),
        ('Cash', 'Cash')
    )
    PAYMENT_STATUSES = (
        ('Paid', 'Paid'),
        ('In process', 'In process'),
        ('Cancelled', 'Cancelled')
    )
    NOTIF_TIMES = (
        (24, 24),
        (6, 6),
        (1, 1)
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=STATUS, max_length=100)

    delivery_address = models.CharField(max_length=250, null=True, blank=True)
    delivery_methods = models.CharField(choices=DELIVERY_METHODS, max_length=100)

    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=100)
    payment_status = models.CharField(choices=PAYMENT_STATUSES, max_length=100, default='In process')
    delivery_notification_before = models.PositiveIntegerField(choices=NOTIF_TIMES, default=6)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class Cashback(models.Model):
    percent = models.PositiveIntegerField()
    treshold = models.PositiveIntegerField()

