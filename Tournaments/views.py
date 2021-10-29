from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return HttpResponse("Welcome to the main page.")

def createLeagueView(request) :
    return HttpResponse("This page is to create a league.")

def updateGamesView(request) :
    return HttpResponse("This page is to update games.")

def rankingsView(request) :
    return HttpResponse("This page is to view rankings.")

def teamInfoView(request) :
    return HttpResponse("This page is to view team info.")

def generateTourneyView(request) :
    return HttpResponse("This page is to generate a tournament.")

