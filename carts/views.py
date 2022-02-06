from django.shortcuts import render

def cart(req):
    return render(req, 'store/carts.html')
