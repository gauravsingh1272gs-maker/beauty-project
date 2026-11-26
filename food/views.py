from django.shortcuts import redirect, render

RESTAURANTS = [
    {'id': 1, 'name': 'The Burger Theory', 'cuisine': 'Burgers • American', 'rating': '4.8', 'time': '20–30 min', 'fee': '0.49', 'image': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85'},
    {'id': 2, 'name': 'Pasta & Vino', 'cuisine': 'Italian • Pasta', 'rating': '4.7', 'time': '25–35 min', 'fee': '1.99', 'image': 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=900&q=85'},
    {'id': 3, 'name': 'Sushi House', 'cuisine': 'Sushi • Japanese', 'rating': '4.9', 'time': '30–40 min', 'fee': '2.49', 'image': 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=900&q=85'},
    {'id': 4, 'name': 'Green Garden', 'cuisine': 'Healthy • Salads', 'rating': '4.6', 'time': '15–25 min', 'fee': '0.99', 'image': 'https://images.unsplash.com/photo-1546793665-c74683f339c1?auto=format&fit=crop&w=900&q=85'},
    {'id': 5, 'name': 'Spice Route', 'cuisine': 'Indian • Curry', 'rating': '4.8', 'time': '25–35 min', 'fee': '1.49', 'image': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=900&q=85'},
    {'id': 6, 'name': 'Casa Tacos', 'cuisine': 'Mexican • Tacos', 'rating': '4.7', 'time': '20–30 min', 'fee': '0.49', 'image': 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=900&q=85'},
]

MENU = {
    1: [('Classic Smash', 'Two beef patties, cheddar, pickles, secret sauce', '12.90', 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=85'), ('Crispy Fries', 'Golden fries with rosemary salt', '4.50', 'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=500&q=85')],
    2: [('Truffle Tagliatelle', 'Fresh pasta, mushroom cream, parmesan', '18.50', 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=500&q=85'), ('Margherita', 'San Marzano tomato, mozzarella, basil', '15.90', 'https://images.unsplash.com/photo-1574072185-9b5f58e6ed9e?auto=format&fit=crop&w=500&q=85')],
    3: [('Sushi Selection', 'Chef’s choice of twelve fresh pieces', '24.90', 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=500&q=85'), ('Salmon Poke', 'Salmon, avocado, edamame, rice', '16.50', 'https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=500&q=85')],
}


def home(request):
    query = request.GET.get('q', '').strip().lower()
    restaurants = RESTAURANTS
    if query:
        restaurants = [r for r in RESTAURANTS if query in (r['name'] + r['cuisine']).lower()]
    return render(request, 'food/home.html', {'restaurants': restaurants, 'query': query})


def restaurant(request, restaurant_id):
    restaurant = next((r for r in RESTAURANTS if r['id'] == restaurant_id), None)
    if not restaurant:
        return redirect('home')
    items = MENU.get(restaurant_id, [
        ('House Special', 'A fresh and flavorful chef selection', '14.90', restaurant['image']),
        ('Side & Drink', 'A tasty side with a refreshing drink', '7.50', 'https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=500&q=85'),
    ])
    return render(request, 'food/restaurant.html', {'restaurant': restaurant, 'items': items})


def add_to_cart(request, restaurant_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        cart = request.session.get('cart', [])
        cart.append({'name': name, 'price': float(price), 'restaurant_id': restaurant_id})
        request.session['cart'] = cart
    return redirect('restaurant', restaurant_id=restaurant_id)


def cart(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] for item in cart)
    return render(request, 'food/cart.html', {'cart': cart, 'subtotal': subtotal, 'total': subtotal + 2.49})


def remove_from_cart(request, index):
    cart = request.session.get('cart', [])
    if 0 <= index < len(cart):
        cart.pop(index)
        request.session['cart'] = cart
    return redirect('cart')


def track_order(request):
    return render(request, 'food/track_order.html')
