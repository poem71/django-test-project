from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural =  "لیست سفارشات"



