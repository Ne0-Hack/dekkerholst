# Generated by Django 4.2.6 on 2023-11-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WWW', '0003_alter_sitesettings_con_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='org_address',
            field=models.CharField(default=1, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
