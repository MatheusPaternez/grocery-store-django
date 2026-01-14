from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'get_total_cost']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(OrderItem)