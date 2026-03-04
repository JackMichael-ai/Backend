from django.db import models


class Item(models.Model):
    # Use ImageField for media support
    image = models.ImageField(upload_to='items/', null=True, blank=True)

    # Use the larger max_length (100) and keep it unique if needed
    title = models.CharField(max_length=100, unique=True)

    description = models.TextField()
    category = models.CharField(max_length=50)

    # DecimalField is superior for currency (no rounding errors)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Track when items are added
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()  # Simple integer for whole numbers
    expirydate = models.DateField()

    def __str__(self):
        return self.name