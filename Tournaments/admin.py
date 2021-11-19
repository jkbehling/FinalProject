from django.contrib import admin
from .models import Player, Team, Tournament, TournamentTeam, Match

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(TournamentTeam)
