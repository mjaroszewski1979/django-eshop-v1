import random

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Category, Product

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    all_products = Product.objects.all()
    similar_products = []
    for item in all_products:
        if item != product:
            similar_products.append(item)

    return render(request, 'product/product.html', {'product': product, 'similar_products': similar_products})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})



