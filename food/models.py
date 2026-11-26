from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(default="Not Provided")
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menu_items"
    )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PREPARING", "Preparing"),
        ("ON_THE_WAY", "On the way"),
        ("DELIVERED", "Delivered"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="PENDING"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"