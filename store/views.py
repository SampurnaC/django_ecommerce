from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Category

def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={'products': products, 'categories': categories}
    return render(request, 'store/home.html', context)

def product_show(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'store/product_show.html', context)

def category_products(request, cat):
    category = Category.objects.get(name=cat)
    category_products = category.products.all()
    context = {'category': category, 'category_products': category_products}
    return render(request, 'store/category_products.html', context)
