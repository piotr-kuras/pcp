# Generated by Django 4.2.8 on 2024-01-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcp', '0002_product_added_by_alter_shop_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='added_by',
        ),
    ]
