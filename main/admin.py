from django.contrib import admin
from .models import Pizza, Order


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'vegetarian', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pizzas', 'custumer_name', 'custumer_phone', 'custumer_address', 'order_date')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order)





