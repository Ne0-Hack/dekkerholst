# Generated by Django 4.2.6 on 2023-11-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/works', verbose_name='загрузить изображение')),
            ],
            options={
                'verbose_name': 'работу',
                'verbose_name_plural': 'работа',
            },
        ),
    ]
