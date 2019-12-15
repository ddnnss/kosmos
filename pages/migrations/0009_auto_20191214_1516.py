# Generated by Django 2.2.7 on 2019-12-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20191130_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicename',
            name='features',
            field=models.TextField(blank=True, null=True, verbose_name='Блок с цифрами. Элементы разделяются точкой с запятой'),
        ),
        migrations.AddField(
            model_name='servicename',
            name='imageHeader',
            field=models.ImageField(null=True, upload_to='services_img/', verbose_name='Изображение для бекграунда страницы с услугой (1920х560)'),
        ),
    ]
