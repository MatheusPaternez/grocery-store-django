from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template import loader
from .models import Category, Product
from .forms import ProductForm

def product_list(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'products.html', context)

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, 'product_form.html',{'form':form,'title':"Add New Product"})

@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_form.html', {'form':form,'title':'Edit Product'})

@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    
    return render(request, 'product_confirm_delete.html', {'product': product})