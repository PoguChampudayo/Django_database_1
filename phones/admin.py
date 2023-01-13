from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name', )}
# Register your models here.
admin.site.register(Phone, PhoneAdmin)