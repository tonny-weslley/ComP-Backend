from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cover_image = models.ImageField(
        upload_to='users/cover', null=True, blank=True)
    joined_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.color + ' - ' + self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(
        upload_to='produtos/coverImages', null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.category.name


class Variation (models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + ' - ' + self.name


class Store (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='stores/logo', null=True, blank=True)
    cover_image = models.ImageField(
        upload_to='stores/cover', null=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.address


class Register (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    last_price = models.DecimalField(max_digits=8, decimal_places=2)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    eddit_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + ' - ' + self.store.name + ' - ' + self.variation.name
