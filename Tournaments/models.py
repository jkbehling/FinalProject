from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    skill_level = models.PositiveIntegerField(default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True)
    team_player = models.ManyToManyField('Player')
    # tournaments = models.ManyToManyField('Tournament', through='TournamentTeam')

    def __str__(self):
        return (self.team_name)


class Tournament(models.Model):
    tourney_name = models.CharField(max_length=50)
    num_teams = models.PositiveIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(8)])

    tournament_teams = models.ManyToManyField('Team', through='TournamentTeam')
    def __str__(self):
        return (self.tourney_name)

class TournamentTeam(models.Model) :
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round = models.IntegerField(default = 1)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s %i %i' %(self.team.team_name, self.tournament.tourney_name, self.round, self.wins, self.losses)

#We didn't end up using this class, but I left it because we might impliment it in the future.
class Match(models.Model) :
    team = models.ForeignKey(TournamentTeam, on_delete=models.CASCADE)
    result = models.CharField(max_length=1)

    def __str__(self):
        return (self.result)

