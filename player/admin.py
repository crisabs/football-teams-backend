from django.contrib import admin
from .models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("nickname", "level", "experience", "coins")
    search_fields = ("nickname",)
    list_filter = ("level",)
