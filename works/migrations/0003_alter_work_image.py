# Generated by Django 4.2.6 on 2023-11-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_work_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, upload_to='works', verbose_name='загрузить изображение'),
        ),
    ]
