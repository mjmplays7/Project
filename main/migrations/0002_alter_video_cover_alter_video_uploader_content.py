# Generated by Django 4.1.4 on 2023-01-15 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(upload_to='videos_uploaded', verbose_name='کاور'),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='contents_uploaded')),
                ('content', models.FileField(upload_to='contents_uploaded')),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('published', 'منتشر شده'), ('unlisted', 'فهرست نشده'), ('private', 'خصوصی')], default='private', max_length=20)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
