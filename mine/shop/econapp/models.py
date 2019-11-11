from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class ProductManager(models.Manager):

    def  all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)
    title = models.CharField(max_length = 120)
    slug = models.SlugField()
    discription = models.TextField(default = 0)
    year = models.IntegerField(default = 2019)
    genre = models.TextField(default = 0)
    material = models.TextField(default = 0)
    image = models.ImageField(upload_to = image_folder)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    available = models.BooleanField(default = True)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_slug': self.slug})

class CartItem(models.Model):
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places = 2, default = 0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.title)


class Cart(models.Model):

    items = models.ManyToManyField(CartItem, blank = True)
    cart_total = models.DecimalField(max_digits=9,  decimal_places = 2, default = 0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()


ORDER_STATUS_CHOICES = (
    ("Принят в обработку", "Принят в обработку"),
    ("Выполняется", "выполняется"),
    ("Оплачен", "Оплачен"),
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    items = models.ManyToManyField(Cart)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length=250)
    buying_type = models.CharField(max_length = 40, choices = (('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')))
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.CharField(max_length=100, choices = ORDER_STATUS_CHOICES)

    def __str__(self):
        return "Заказ №{0}".format(str(self.id))


