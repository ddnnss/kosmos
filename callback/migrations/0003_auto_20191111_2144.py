# Generated by Django 2.2.7 on 2019-11-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0002_auto_20191111_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question1',
            field=models.CharField(blank=True, default='Нет ответа', max_length=255, null=True, verbose_name='Обслуживались ли Вы ранее у сторонней бухгалтерии?'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question2',
            field=models.CharField(blank=True, default='Нет ответа', max_length=255, null=True, verbose_name='Количество штатных единиц?'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question3',
            field=models.CharField(blank=True, default='Нет ответа', max_length=255, null=True, verbose_name='Количество операций ?'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question4',
            field=models.CharField(blank=True, default='Нет ответа', max_length=255, null=True, verbose_name='Система налогообложения?'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question5',
            field=models.CharField(blank=True, default='Нет ответа', max_length=255, null=True, verbose_name='Количество контрагентов?'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='userName',
            field=models.CharField(blank=True, default='Нет данных', max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='userPhone',
            field=models.CharField(blank=True, default='Нет данных', max_length=255, null=True, verbose_name='Телефон'),
        ),
    ]