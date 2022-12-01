# Generated by Django 4.1.1 on 2022-10-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11)),
                ('code', models.SmallIntegerField()),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
