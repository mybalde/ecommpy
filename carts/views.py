from django.shortcuts import redirect, render

from store.models import Product
from .models import Cart,CartItem

def cart(req):
    return render(req, 'store/carts.html')

def _get_cart_id(req):
    '''get cart id from request session'''
    return id if (id := req.session.session_key) else req.session.create()
    
        

def add_cart(req, produit_id):
    '''add a product in the cart'''
    product = Product.objects.get(product_name=produit_id)
    try:
        cart = Cart.objects.get(cart_id = _get_cart_id(req))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _get_cart_id(req))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
    except CartItem.DoesNotExist: 
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
    cart_item.save()
    return redirect('cart')
