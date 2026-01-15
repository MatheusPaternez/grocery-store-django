from django.urls import path
from . import views

urlpatterns = [
    # customer routes
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.my_cart, name='my_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # staff routes
    path('approve/<int:order_id>/', views.approve_order, name='approve_order'),
    path('deny/<int:order_id>/', views.deny_order, name='deny_order'),
]