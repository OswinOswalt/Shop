from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from econapp.forms import OrderForm
from econapp.models import Category, Product, CartItem, Cart



def first_page(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart

    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    product = Product.objects.get(slug = product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug = category_slug)
    products_of_category = Product.objects.filter(category = category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories,
    }
    return render(request, 'category.html', context)


def dellivery(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dellivery.html', context)


def installment(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'installment.html', context)


def cart_view(request):
    categories = Category.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    context = {
        'cart': cart,
        'categories': categories,
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request, product_slug):

    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))


def remove_from_cart_view(request, product_slug):
        try:
            cart_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)
        product = Product.objects.get(slug=product_slug)
        cart.remove_from_cart(product.slug)
        new_cart_total = 0.00
        for item in cart.items.all():
            new_cart_total+=float(item.item_total)
        cart.cart_total = new_cart_total
        cart.save()
        return HttpResponseRedirect(reverse('cart'))


def checkout_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context ={
        'cart': cart
    }
    return render(request, 'checkout.html', context)


def order_create_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'order.html', context)

