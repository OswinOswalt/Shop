from django.contrib import admin
from econapp.models import Category,  Product, CartItem, Cart, Profile, Order

admin.site.register(Category)
# admin.site.register(Author)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Order)

# Register your models here.
