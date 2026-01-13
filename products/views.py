from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category

def product_list(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'products.html', context)
