# Generated by Django 4.1.4 on 2023-01-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_content_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
