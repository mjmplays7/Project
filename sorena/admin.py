from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Sorena_User)
class   Sorena_UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ["name", "last","national_id", "number"]
        }),
        ("Birthday", {
            "fields": ["birthday", "birthmonth", "birthyear"]
        }),
        ("Insurance", {
            "fields": ["start_insurance_day","start_insurance_month", "start_insurance_year", "end_insurance_year"]
        }),
        ("Aditional", {
            "fields": ["field","coach"]
        })
    ]
    readonly_fields = []
    list_display = ["name", "last", "national_id", "number"]
    list_filter = ["name", "last", "national_id"]
    search_fields = ["name", "last", "national_id"]

admin.site.register(Admin)
admin.site.register(Coach)
admin.site.register(Field)
