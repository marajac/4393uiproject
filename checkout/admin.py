from django.contrib import admin

# Register your models here.
from .models import summary

class summaryAdmin(admin.ModelAdmin):
    class Meta:
        model = summary

admin.site.register(summary, summaryAdmin)
