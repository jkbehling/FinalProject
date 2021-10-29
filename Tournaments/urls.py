from django.urls import path
from .views import indexPageView, createLeagueView, updateGamesView, rankingsView, teamInfoView, generateTourneyView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Leagueview/", createLeagueView, name="league"),
    path("Update/", updateGamesView, name="update"),
    path("Rankings/", rankingsView, name="ranking"),
    path("TeamInfo/", teamInfoView, name="info"),
    path("Generate/", generateTourneyView, name="generate"),

]