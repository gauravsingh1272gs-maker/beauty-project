from django.contrib import admin
from .models import MenuItem, Order, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "is_open")
    search_fields = ("name", "address")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "price", "is_available")
    list_filter = ("restaurant", "is_available")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "restaurant", "total_price", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username", "restaurant__name")