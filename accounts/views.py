from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from orders.models import Order

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        # Pass context too ({'form':form})
    return render(request,'registration/register.html', {'form':form})
    
def check_is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(check_is_staff)
def staff_panel(request):
    orders = Order.objects.filter(status='PENDING').order_by('-created_at')
    
    context = {
        'orders':orders
    }
    return render(request, 'staff_panel.html',context)