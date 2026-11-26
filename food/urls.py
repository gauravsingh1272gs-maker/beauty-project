from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant, name='restaurant'),
    path('restaurant/<int:restaurant_id>/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:index>/', views.remove_from_cart, name='remove_from_cart'),
    path('track-order/', views.track_order, name='track_order'),
]
