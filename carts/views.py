from django.shortcuts import get_object_or_404, redirect, render

from store.models import Product
from .models import Cart,CartItem

def _get_cart_id(req):
    '''get cart id from request session'''
    return id if (id := req.session.session_key) else req.session.create()
    
def cart(req):
    context = {'quantity': 0, 'total': 0 }
    try:
        cart = Cart.objects.get(cart_id = _get_cart_id(req))
        cart_items = CartItem.objects.filter(cart=cart)
        context['cart_items'] = cart_items
        for cart_item in cart_items:
            context['total'] += cart_item.sub_total()
            context['quantity'] += cart_item.quantity
    except: 
        pass

    return render(req, 'store/carts.html', context) 

def add_cart(req, product_id):
    '''add a product in the cart'''
    product = Product.objects.get(product_name=product_id)
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

def remove_cart(req, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(req))
    product = get_object_or_404(Product, product_name=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

def remove(req, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(req))
    product = get_object_or_404(Product, product_name=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    
    return redirect('cart')