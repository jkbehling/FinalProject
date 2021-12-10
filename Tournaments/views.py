from django.shortcuts import render
from django.http import HttpResponse
from Tournaments.models import Team, Player, TournamentTeam, Tournament

# Create your views here.

def indexPageView(request) :
    return render(request, 'tournaments/index.html')

def createLeagueView(request) :
    
    newTourney = Tournament()
    tourneyName = request.POST['name']
    newTourney.tourney_name = tourneyName
    newTourney.num_teams = 8
    newTourney.save()
    
    newTourneyTeam = Team.objects.get(id = request.POST['team1'])
    
    
    def createTournamentTeam(team, tournament):
        newTournament = TournamentTeam()
        newTournament.team = team
        newTournament.tournament = tournament
        newTournament.round = 1
        newTournament.wins = 0
        newTournament.losses = 0
        newTournament.save()

    
    createTournamentTeam(newTourneyTeam, newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team2']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team3']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team4']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team5']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team6']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team7']), newTourney)
    createTournamentTeam(Team.objects.get(id = request.POST['team8']), newTourney)
    
    newTourney.save()


    tourneyData = newTourney.tournament_teams.all()
    tourneyID = newTourney.id
    record = TournamentTeam.objects.filter(tournament_id=tourneyID)
    



    context = {
        "teams": tourneyData,
        "tourneyID": tourneyID,
        "record": record,
        "tourneyName": tourneyName,
    }
        
    return render(request, 'tournaments/bracket.html', context)
        

def bracketView(request) :
    
    bracketData = Tournament.objects.all()

    context = {
        "bracket" : bracketData,
    }
    
    return render(request, 'tournaments/bracketView.html', context)

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
    teamData = Team.objects.all()
    context = {
        "team": teamData
    }
    return render(request, 'tournaments/generateTourney.html', context)

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

def addTeamViews(request) :

    return render(request, 'tournaments/add_team.html')

def createTeam(request) :
    teamName = request.POST['team_name']
    newTeam = Team()
    newTeam.team_name = teamName
    newTeam.save()

    teamData = Team.objects.get(id = newTeam.id)
    context = {
        "team" : teamData
    }

    return render(request, 'tournaments/add_member.html', context)

def deleteTeam(request, team_id) :
    teamData = Team.objects.get(id=team_id)
    teamData.delete()

    data = Team.objects.all()
    context = {
        "team" : data
    }
    return render(request, 'tournaments/viewTeams.html', context)

def advanceTeam(request, tournament_id, id) :
    currentTourney = TournamentTeam.objects.filter(tournament_id=tournament_id)
    currentTeam = TournamentTeam.objects.get(id=id)
    currentTeam.wins += 1
    currentTeam.round += 1
    currentTeam.save()
    tourneyName = Tournament.objects.get(id=tournament_id)
    
    currentID = tournament_id
    context = {
        "record" : currentTourney,
        "tourneyID": currentID,
        "tourneyName": tourneyName
    }
    return render(request, 'tournaments/bracket.html', context)

def TournamentResultsView(request) :
    tournament = TournamentTeam.objects.filter(tournament=request.POST.get("tourneyID")).order_by("-wins")

    context = {
        "tournament": tournament
    }
    return render(request, 'tournaments/results.html', context)
