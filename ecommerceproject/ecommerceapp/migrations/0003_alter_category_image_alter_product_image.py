# Generated by Django 4.1 on 2022-11-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_rename_availabe_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
