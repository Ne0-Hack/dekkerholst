# Generated by Django 4.2.6 on 2023-11-01 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_categoryorder_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='production',
        ),
    ]
