from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from products.models import Product

def home(request):
    featured_products = Product.objects.all()[:4]
    
    context = {
        'featured_products': featured_products
    }
    return render(request, 'home.html', context)