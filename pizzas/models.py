from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    pizzas = models.ManyToManyField('Pizza', related_name='orders')
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'
    

# Ingredients of pizza
class Topping(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='pizzas/images/')
    toppings = models.ManyToManyField(Topping, related_name='pizzas')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name