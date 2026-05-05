from django.contrib import admin
from .models import Team, PlayerTeam, PlayerProposalTeam


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "nickname", "city", "country", "founder", "owner")
    search_fields = ("name", "nickname", "city", "country")
    list_filter = ("city", "country")


@admin.register(PlayerTeam)
class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ("player", "team", "membership_date", "matches_played")
    search_fields = ("player__user__username", "team__name")
    list_filter = ("membership_date",)


@admin.register(PlayerProposalTeam)
class PlayerProposalTeamAdmin(admin.ModelAdmin):
    list_display = ("player", "team")
    search_fields = ("player__user__username", "team__name")
    list_filter = ("team__name",)
