# Generated by Django 3.1 on 2020-08-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_variant',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
