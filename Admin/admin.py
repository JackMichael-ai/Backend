from django.contrib import admin
from django.contrib.auth.models import User
from Admin.models import Item, Product

# Register your models here.
admin.site.register(Item)
admin.site.register(Product)