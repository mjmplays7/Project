from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = "published")

class Video(models.Model):
    STATUS_OF_VIDEOS = (
        ("published", "منتشر شده"),
        ("unlisted", "فهرست نشده"),
        ("private", "خصوصی")
    )

    title = models.CharField(_("عنوان"), max_length = 255)
    description = models.TextField(_("توضیحات"), blank = True)
    content = models.FileField(_("ویدیو"), upload_to = 'videos_uploaded',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]) 
    cover = models.ImageField(_("کاور"), upload_to = 'videos_uploaded')
    uploaded = models.DateTimeField(_("تاریخ انتشار"), auto_now_add = True)
    edited = models.DateTimeField(_("تاریخ ویرایش"), auto_now = True)
    uploader = models.ForeignKey(User, on_delete = models.CASCADE, related_name="videos")
    status = models.CharField(_("وضعیت"), max_length = 20, choices = STATUS_OF_VIDEOS, default = "private")
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(self.id)
            self.save()

    def get_absolute_url(self):
        return reverse("main:content", kwargs = {"slug": self.slug})
    
    
    
    def __str__(self):
        return f"{self.uploader}: {self.title} {self.uploaded}"
    class Meta:
        ordering = ("-uploaded",)
    
    objects = models.Manager()
    publish = PublishedManager()


class Content(models.Model):
    STATUS_OF_VIDEOS = (
        ("published", "منتشر شده"),
        ("unlisted", "فهرست نشده"),
        ("private", "خصوصی")
    )


    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to= 'contents_uploaded')
    content = models.FileField(upload_to = 'contents_uploaded')
    price = models.PositiveIntegerField()
    status = models.CharField(max_length = 20, choices = STATUS_OF_VIDEOS, default = "private")
    uploaded = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    uploader = models.ForeignKey(User, on_delete = models.CASCADE, related_name="contents")
    slug = models.SlugField(unique = True)



    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(self.id)
            self.save()

    def get_absolute_url(self):
        return reverse("main:edu_content", kwargs = {"slug": self.slug})

    def __str__(self):
        return f"Title: {self.title}, id: {self.id}"


    objects = models.Manager()
    publish = PublishedManager()

class Main_User(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE, related_name="users")
    bought = models.ManyToManyField(Content, blank=True,related_name="main_users")
    number = models.CharField(default=00000000000, max_length=11, validators=[MinLengthValidator(11)])
    
    def __str__(self):
        bought = ','.join(str(b) for b in self.bought.all())
        return f"{bought}"


class User_Order(models.Model):
    username = models.CharField(max_length=400)
    order = models.CharField(max_length=400)

    def __str__(self):
        return f"Username: {self.username}, Order: {self.order}"
