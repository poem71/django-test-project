from django.db import models
from datetime import date

class Order(models.Model):
    DATE_FORMAT = "%Y-%m-%d"


    PRODUCT_TYPES = [
        ('میلگرد', 'میلگرد'),
        ('تیرآهن', 'تیرآهن'),
        ('کلاف', 'کلاف'),
        ('ورق', 'ورق'),
    ]

    # فیلدهای جدید اضافه شدند
    date = models.DateField(default=date.today,verbose_name="تاریخ")
    product_type = models.CharField(max_length=50, default="میلگرد",verbose_name="نوع کالا")
    size = models.CharField(max_length=100, default="نامشخص",verbose_name="سایز کالا")
    requester_name = models.CharField(max_length=100, default="ناشناخته",verbose_name="نام درخواست ‌کننده")
    quantity = models.PositiveIntegerField(verbose_name="مقدار درخواست")  # مقدار درخواست
    manufacturer = models.CharField(max_length=100, default="Unknown",verbose_name="کارخانه تولید‌کننده")
    unloading_place = models.CharField(max_length=100, default="ناشناخته",verbose_name="محمل تخلیه")
    description = models.TextField(blank=True, null=True,verbose_name="شرح درخواست")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "لیست سفارشات"

