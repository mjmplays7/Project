# Generated by Django 4.1.4 on 2023-01-11 07:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('content', models.FileField(upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='ویدیو')),
                ('cover', models.ImageField(upload_to='image_uploaded', verbose_name='کاور')),
                ('uploaded', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('status', models.CharField(choices=[('published', 'منتشر شده'), ('unlisted', 'فهرست نشده'), ('private', 'خصوصی')], default='private', max_length=20, verbose_name='وضعیت')),
                ('slug', models.SlugField(unique=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded',),
            },
        ),
    ]