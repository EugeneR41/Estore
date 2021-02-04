# Generated by Django 3.1.5 on 2021-02-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_payment_intent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('arrived', 'Arrived')], default='ordered', max_length=20),
        ),
    ]
