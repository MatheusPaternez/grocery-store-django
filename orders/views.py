from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .models import Order, OrderItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    order, created = Order.objects.get_or_create(user=request.user, status='CART')

    order_item, item_created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'price': product.price} 
    )

    if not item_created:
        order_item.quantity += 1
        order_item.save()
        messages.success(request, f"Added another {product.name} to your cart")
    else:
        messages.success(request, f"{product.name} added to your cart")
    
    return redirect('products')

@login_required
def my_cart(request):
    try:
        order = Order.objects.get(user=request.user, status='CART')
    except Order.DoesNotExist:
        order = None

    return render(request, 'my_cart.html',{'order':order})

@login_required
def checkout(request):
    try:
        order = Order.objects.get(user=request.user, status='CART')
        order.status = 'PENDING' # transform the cart to a pending order
        order.save()
        messages.success(request, "Order sent for approval. Check back soon")
    except Order.DoesNotExist:
        messages.error(request, "No active cart found.")
        
    return redirect('home')

@staff_member_required
@require_POST
def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'APPROVED'
    order.save()
    return redirect('staff_panel')

@staff_member_required
@require_POST
def deny_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'DENIED'
    order.save()
    return redirect('staff_panel')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).exclude(status='CART').order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})