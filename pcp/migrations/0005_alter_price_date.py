# Generated by Django 4.2.8 on 2024-01-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcp', '0004_alter_price_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
