from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(req, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    context = {'products': products, 'products_count': products_count}

    return render(req, 'store/store.html', context)

def product_detail(req, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {'product': product}

    return render(req, 'store/product_detail.html', context)
