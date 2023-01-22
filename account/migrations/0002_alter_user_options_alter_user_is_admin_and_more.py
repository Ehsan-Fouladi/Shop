# Generated by Django 4.1.1 on 2022-10-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربر ها'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='ادمین'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن'),
        ),
    ]