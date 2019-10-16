from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(SuccessFactor,PerformanceIndicator)
class ViewAdmin(admin.ModelAdmin):
    pass

