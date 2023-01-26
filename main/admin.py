from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Video)
class   VideoAdmin(admin.ModelAdmin):
    #fields = ["title", "uploader", "uploaded", "edited"]
    
    fieldsets = [
        (None, {
            "fields": ["title", "description","status"]
        }),
        ("Content", {
            "fields": ["content", "cover"]
        }),
        ("Aditional", {
            "fields": ["slug","uploaded", "edited", "uploader"]
        })
    ]
    readonly_fields = ["uploaded", "edited","slug"]
    list_display = ["title", "uploader", "status", "uploaded"]
    list_filter = ["status"]
    search_fields = ["title", "uploader__username"]


# another way:
#class   VideoAdmin(admin.ModelAdmin):
#    list_display = ["title", "uploader", "status"]
#    list_filter = ["status"]
#    search_fields = ["title", "uploader__username"]

@admin.register(Content)
class   ContentAdmin(admin.ModelAdmin):
    #fields = ["title", "uploader", "uploaded", "edited"]
    
    fieldsets = [
        (None, {
            "fields": ["title", "description","status", "price"]
        }),
        ("Content", {
            "fields": ["content", "cover"]
        }),
        ("Aditional", {
            "fields": ["slug","uploaded", "edited", "uploader"]
        })
    ]
    readonly_fields = ["uploaded", "edited","slug"]
    list_display = ["title", "uploader", "status", "uploaded"]
    list_filter = ["status"]
    search_fields = ["title", "uploader__username"]

admin.site.register(User_Order)
admin.site.register(Main_User)