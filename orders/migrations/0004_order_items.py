# Generated by Django 4.1.7 on 2023-02-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_items_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='orders.item'),
        ),
    ]
