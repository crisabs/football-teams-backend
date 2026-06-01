from django.contrib import admin
from achievement.models import Achievement, PlayerAchievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "description")


@admin.register(PlayerAchievement)
class PlayerAchievementAdmin(admin.ModelAdmin):
    list_display = ("player", "achievement_name", "acquired_at")

    list_select_related = ("player",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("achievements")

    @admin.display(description="Achievement", ordering="achievement_name")
    def achievement_name(self, obj):
        return ", ".join([achievement.name for achievement in obj.achievements.all()])
