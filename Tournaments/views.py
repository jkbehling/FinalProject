from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return render(request, 'tournaments/index.html')
    #return HttpResponse("Hi")

def createLeagueView(request) :
    return render(request, 'tournaments/index.html')

def updateGamesView(request) :
    return render(request, 'tournaments/index.html')

def rankingsView(request) :
    return render(request, 'tournaments/index.html')

def teamInfoView(request) :
    return render(request, 'tournaments/index.html')

def generateTourneyView(request) :
    return render(request, 'tournaments/index.html')

