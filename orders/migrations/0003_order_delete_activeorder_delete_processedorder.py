# Generated by Django 4.2.6 on 2023-10-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_processedorder_rename_order_activeorder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, verbose_name='статус заказа')),
            ],
            options={
                'verbose_name': 'активные заказы',
                'verbose_name_plural': 'активный',
            },
        ),
        migrations.DeleteModel(
            name='ActiveOrder',
        ),
        migrations.DeleteModel(
            name='ProcessedOrder',
        ),
    ]
