# Generated by Django 4.1.1 on 2023-01-26 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'ادرس کاربرها'},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='number',
            new_name='phone',
        ),
    ]