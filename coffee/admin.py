from django.contrib import admin
from .models import Coffee, Order, OrderItem
    

admin.site.register(Coffee)
admin.site.register(Order)
admin.site.register(OrderItem)