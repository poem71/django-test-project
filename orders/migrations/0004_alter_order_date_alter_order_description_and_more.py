# Generated by Django 5.1.2 on 2025-02-04 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_options_remove_order_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='شرح درخواست'),
        ),
        migrations.AlterField(
            model_name='order',
            name='manufacturer',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='کارخانه تولید\u200cکننده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_type',
            field=models.CharField(default='میلگرد', max_length=50, verbose_name='نوع کالا'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='مقدار درخواست'),
        ),
        migrations.AlterField(
            model_name='order',
            name='requester_name',
            field=models.CharField(default='ناشناخته', max_length=100, verbose_name='نام درخواست \u200cکننده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(default='نامشخص', max_length=100, verbose_name='سایز کالا'),
        ),
        migrations.AlterField(
            model_name='order',
            name='unloading_place',
            field=models.CharField(default='ناشناخته', max_length=100, verbose_name='محمل تخلیه'),
        ),
    ]
