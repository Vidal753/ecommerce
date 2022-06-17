import math

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, verbose_name='Nombre')
    email = models.CharField(max_length=200, null=True, verbose_name='Correo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Producto')
    price = models.FloatField(verbose_name='Precio')
    digital = models.BooleanField(default=False, null=True, blank=False)
    # remember install pillow before
    image = models.ImageField(null=True, blank=True, verbose_name='Imagen')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cliente')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pedido')
    completed = models.BooleanField(default=False, null=True, blank=False, verbose_name='Completada')
    transaction_id = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    def total(self):
        orderItem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItem])
        return math.floor(total)

    def productos(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        order_item = self.orderitem_set.all()
        for item in order_item:
            if not item.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderItem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItem])
        return total

    @property
    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Producto')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Orden')
    quantity = models.IntegerField(default=0, null=True, blank=True,verbose_name= 'Cantidad')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pedido')

    class Meta:
        verbose_name = 'Orden de Producto'
        verbose_name_plural = 'Ordenes de Productos'

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShoppingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cliente')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Orden')
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True, verbose_name='Cuidad')
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.address
