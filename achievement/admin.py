from django.contrib import admin
from achievement.models import Achievement, PlayerAchievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "description")


@admin.register(PlayerAchievement)
class PlayerAchievementAdmin(admin.ModelAdmin):
    list_display = ("player", "achievement_name", "description", "acquired_at")

    list_select_related = ("player", "achievement")

    @admin.display(description="Achievement", ordering="achievement__name")
    def achievement_name(self, obj):
        return obj.achievement.name
