# Generated by Django 4.1.4 on 2023-01-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_order_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_order',
            name='username',
            field=models.CharField(max_length=400),
        ),
    ]