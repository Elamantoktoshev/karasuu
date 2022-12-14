# Generated by Django 3.2.12 on 2022-11-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('ad_client', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('ad_discription', models.CharField(max_length=200, verbose_name='Описания реклама')),
                ('ad_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('ad_social', models.CharField(max_length=20, verbose_name='Соц. сети')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
