# Generated by Django 4.2.6 on 2023-11-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_alter_productionorder_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='price',
            field=models.IntegerField(help_text='Например: 1000', null=True, verbose_name='Цена'),
        ),
    ]