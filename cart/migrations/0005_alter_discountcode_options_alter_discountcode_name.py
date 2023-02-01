# Generated by Django 4.1.1 on 2023-02-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_discountcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discountcode',
            options={'verbose_name': 'کد تخفیف کاربران', 'verbose_name_plural': 'کد تخفیف'},
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='name',
            field=models.CharField(max_length=7, unique=True, verbose_name='کد تخفیف'),
        ),
    ]
