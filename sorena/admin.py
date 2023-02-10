from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Sorena_User)
class   Sorena_UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ["name", "last","national", "number"]
        }),
        ("Birthday", {
            "fields": ["birthday", "birthmonth", "birthyear"]
        }),
        ("Insurance", {
            "fields": ["start_insurance_day","start_insurance_month", "start_insurance_year"]
        }),
        ("Aditional", {
            "fields": ["field","coach"]
        })
    ]
    readonly_fields = []
    list_display = ["name", "last", "national", "number"]
    list_filter = ["name", "last", "national"]
    search_fields = ["name", "last", "national"]

admin.site.register(Admin)
admin.site.register(Coach)
admin.site.register(Field)
admin.site.register(Gym)

@admin.register(Time)
class   TimeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ["field", "coach","gym"]
        }),
        ("time", {
            "fields": ["day", "time"]
        })
    ]
    readonly_fields = []
    list_display = ["field", "coach", "gym", "day", "time"]
    list_filter = ["field", "coach", "gym"]
    search_fields = ["field", "coach", "gym"]