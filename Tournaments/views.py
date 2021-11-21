from django.shortcuts import render
from django.http import HttpResponse
from Tournaments.models import Team, Player

# Create your views here.

def indexPageView(request) :
    return render(request, 'tournaments/index.html')
    #return HttpResponse("Hi")

def createLeagueView(request, name) :
    return render(request, name, 'tournaments/index.html')

def updateGamesView(request) :
    return render(request, 'tournaments/index.html')

def rankingsView(request) :
    return render(request, 'tournaments/index.html')

def teamInfoView(request) :
    data = Team.objects.all()
    context = {
        "team" : data
    }
    return render(request, 'tournaments/viewTeams.html', context)

def teamMembersView(request, team_id) :
    teamData = Team.objects.get(id = team_id)
    playerData = teamData.team_player.all()
    context = {
        "player" : playerData,
        "team" : teamData
    }
    return render(request, 'tournaments/team_members.html', context)
    


def generateTourneyView(request) :
    return render(request, 'tournaments/generateTourney.html')

def addTeamMember(request, team_id) :
    teamData = Team.objects.get(id = team_id)
    playerData = teamData.team_player.all()
    context = {
        "player" : playerData,
        "team" : teamData
    }
    if request.method == 'POST' :
        player = Player()

        player.first_name = request.POST['first_name']
        player.last_name = request.POST['last_name']
        player.skill_level = request.POST['skill']

        player.save()

        teamData.team_player.add(player)

        return teamMembersView(request, team_id)

    else :
        return render(request, 'tournaments/add_member.html', context)

def removeTeamPlayer(request, team_id, team_player_id) :
    teamData = Team.objects.get(id = team_id)
    playerData = teamData.team_player.get(id = team_player_id)
    
    playerData.delete()

    return teamMembersView(request, team_id)


