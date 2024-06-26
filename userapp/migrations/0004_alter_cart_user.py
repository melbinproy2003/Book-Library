# Generated by Django 5.0.3 on 2024-04-29 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestapp', '0004_alter_logintable_id_alter_usertable_id'),
        ('userapp', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='guestapp.usertable'),
        ),
    ]
