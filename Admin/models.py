from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    expirydate = models.DateField()

    def __str__(self):
        return self.name