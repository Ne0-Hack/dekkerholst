# Generated by Django 4.2.6 on 2023-11-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_alter_order_status_delete_statusorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='upload',
            field=models.ImageField(blank=True, upload_to='orders/', verbose_name='загрузить изображение'),
        ),
    ]
