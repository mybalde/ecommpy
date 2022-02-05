from django.shortcuts import render
from .models import Product
from category.models import Category

def store(req):
    products = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    categories = Category.objects.all().order_by('category_name')
    context = {'products': products,
               'products_count': products_count, 'categories': categories}
    return render(req, 'store/store.html', context)
