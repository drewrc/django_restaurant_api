# Generated by Django 4.1.7 on 2023-02-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_itemname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='itemname',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='orders.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='itemname',
            field=models.ManyToManyField(related_name='order_names', to='orders.item'),
        ),
    ]
