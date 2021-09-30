from django.db import models
from django.utils import timezone

class ItemModel(models.Model):
    item_name = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    quantity_unit = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    total_price = models.BigIntegerField(null=True)
    def __str__(self):
        return "%s %s" % (self.item_name,self.quantity)

class CustomerModel(models.Model):
    customer_id = models.IntegerField(primary_key = True)
    customer_name = models.CharField(max_length=200,null=True,blank=True)
    customer_mobile_number = models.BigIntegerField(null=True,blank=True)
    def __str__(self):
        return self.customer_name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True)
    items = models.ManyToManyField('ItemModel', related_name='order')
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
