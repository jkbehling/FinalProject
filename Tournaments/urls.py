from django.urls import path
from .views import indexPageView, createLeagueView, updateGamesView, rankingsView, teamInfoView, generateTourneyView, teamMembersView, addTeamMember
from .views import removeTeamPlayer, addTeamViews, bracketView, createTeam, deleteTeam, advanceTeam, TournamentResultsView
urlpatterns = [
    path("", indexPageView, name="index"),
    path("Leagueview/", createLeagueView, name="league"),
    path("Update/", updateGamesView, name="update"),
    path("Rankings/", rankingsView, name="ranking"),
    path("TeamInfo/", teamInfoView, name="info"),
    path("Generate/", generateTourneyView, name="generate"),
    path("TeamMembers/<int:team_id>/", teamMembersView, name="team_members"),
    path("AddMember/<int:team_id>/", addTeamMember, name="add_member"),
    path("removeTeamPlayer/<int:team_id>/<int:team_player_id>/", removeTeamPlayer, name="removeTeamPlayer"),
    path("AddTeam/", addTeamViews, name="add_team"),
    path("Bracket/", bracketView, name="bracket"),
    path("CreateTeam/", createTeam, name="create_team"),
    path("DeleteTeam/<int:team_id>/", deleteTeam, name="delete_team"),
    path("AdvanceTeam/<int:tournament_id>/<int:id>/", advanceTeam, name="advance"),
    path("Results/", TournamentResultsView, name="results"),
]