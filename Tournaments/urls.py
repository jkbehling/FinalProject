from django.urls import path
from .views import indexPageView, createLeagueView, updateGamesView, rankingsView, teamInfoView, generateTourneyView, teamMembersView, addTeamMember

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Leagueview/", createLeagueView, name="league"),
    path("Update/", updateGamesView, name="update"),
    path("Rankings/", rankingsView, name="ranking"),
    path("TeamInfo/", teamInfoView, name="info"),
    path("Generate/", generateTourneyView, name="generate"),
    path("TeamMembers/<int:team_id>/", teamMembersView, name="team_members"),
    path("AddMember/<int:team_id>/", addTeamMember, name="add_member")
]