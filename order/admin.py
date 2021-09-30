from django.contrib import admin
from .models import *

admin.site.register(ItemModel)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)
# Register your models here.
