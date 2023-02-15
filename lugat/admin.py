from django.contrib import admin
from .models import *

@admin.register(Togri)
class TogriAdmin(admin.ModelAdmin):
    list_display = ('id', "soz")

@admin.register(NoTogri)
class NotogriAdmin(admin.ModelAdmin):
    list_display = ("id", "notogri", "t_soz", )
