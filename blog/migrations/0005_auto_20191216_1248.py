# Generated by Django 2.2.7 on 2019-12-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='blog_img/', verbose_name='Изображение превью (555 x 390)'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='name',
            field=models.CharField(max_length=120, null=True, verbose_name='Название (120 символов)'),
        ),
    ]
