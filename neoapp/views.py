from django.shortcuts import render, redirect
from .forms import PlayerForm, CoachForm, TeamForm, AssignPlayerToTeamForm, AssignCoachToPlayer, ConnectTeammatesForm, AssignCoachToTeamForm
from .models import Player, Team, Coach
from django.contrib import messages

def home_view(request):
    players = Player.nodes.all()
    teams = Team.nodes.all()
    coaches = Coach.nodes.all()

    # Relationships between Players and Teams
    player_team_connections = []
    for player in players:
        team = player.team.single()
        if team:
            player_team_connections.append((player.name, team.name))

    # Relationships between Coaches and Players
    coach_player_connections = []
    for coach in coaches:
        for player in coach.coaches:
            coach_player_connections.append((coach.name, player.name))

    # Relationships between Coaches and Team
    coach_team_connections = []
    for coach in coaches:
        for team in coach.team:
            coach_team_connections.append((coach.name, team.name))

    # Relationships between Teammates
    teammates_connections = []
    for player in players:
        for teammate in player.teammates:
            teammates_connections.append((player.name, teammate.name))

    context = {
        'players': players,
        'teams': teams,
        'coaches': coaches,
        'player_team_connections': player_team_connections,
        'coach_player_connections': coach_player_connections,
        'coach_team_connections': coach_team_connections,
        'teammates_connection': teammates_connections,
    }

    return render(request, 'neoapp/home.html', context)

def player_list(request):
    players = Player.nodes.all()
    return render(request, 'neoapp/player_list.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = Player(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                height = form.cleaned_data['height'],
                number = form.cleaned_data['number'],
                weight = form.cleaned_data['weight']
            ).save()
            return redirect('player_list')
    else:
        form = PlayerForm()
        return render(request, 'neoapp/add_player.html', {'form': form})


def team_list(request):
    teams = Team.nodes.all()
    return render(request, 'neoapp/team_list.html', {'teams': teams})


def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = Team(
                name = form.cleaned_data['name']
            ).save()
            return redirect('team_list')
    else:
        form = TeamForm()
        return render(request, 'neoapp/add_team.html', {'form': form})


def coach_list(request):
    coaches = Coach.nodes.all()
    return render(request, 'neoapp/coach_list.html', {'coaches': coaches})


def add_coach(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            coach = Coach(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age']
            ).save()
            return redirect('coach_list')
    else:
        form = CoachForm()
        return render(request, 'neoapp/add_coach.html', {'form': form})
    

def assign_player_to_team(request):
    if request.method == 'POST':
        form = AssignPlayerToTeamForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['player']  # Capture the player's name as String to search the player by his name
            team_name = form.cleaned_data['team']  # Capture the team's name as String to search the team by its name
            player = Player.nodes.first(name=player_name) 
            team = Team.nodes.first(name=team_name)
            player.team.connect(team)
            messages.success(request, f'{player.name} assigned to {team.name}')
            return redirect('player_to_team')
    else:
        form = AssignPlayerToTeamForm()
        return render(request, 'neoapp/assign_player_to_team.html', {'form': form})


def assign_coach_to_player(request):
    if request.method == 'POST':
        form = AssignCoachToPlayer(request.POST)
        if form.is_valid():
            coach_name = form.cleaned_data['coach']
            player_name = form.cleaned_data['player']
            coach = Coach.nodes.first(name=coach_name)
            player = Player.nodes.first(name=player_name)
            coach.coaches.connect(player)
            messages.success(request, f'{coach.name} connected to {player.name}')
            return redirect('coach_to_player')
    else:
        form = AssignCoachToPlayer()
        return render(request, 'neoapp/assign_coach_to_player.html', {'form': form})
    
    
def assign_coach_to_team(request):
    if request.method == 'POST':
        form = AssignCoachToTeamForm(request.POST)
        if form.is_valid():
            coach_name = form.cleaned_data['coach']
            team_name = form.cleaned_data['team']
            coach = Coach.nodes.first(name=coach_name)
            team = Team.nodes.first(name=team_name)
            coach.team.connect(team)
            messages.success(request, f'{coach.name} connected to {team.name}')
            return redirect('coach_to_team')
    else:
        form = AssignCoachToTeamForm()
        return render(request, 'neoapp/assign_coach_to_team.html', {'form': form})


def ConnectTeammates(request):
    if request.method == 'POST':
        form = ConnectTeammatesForm(request.POST)
        if form.is_valid():
            player1_name = form.cleaned_data['player1']
            player2_name = form.cleaned_data['player2']
            player1 = Player.nodes.first(name=player1_name)
            player2 = Player.nodes.first(name=player2_name)
            if player1_name == player2_name:
                messages.error(request, f'{player1.name} can NOT be connected to {player2.name} because is the same player')
            else:
                player1.teammates.connect(player2)
                player2.teammates.connect(player1)
                messages.success(request, f'{player1.name} connected to {player2.name}')
                return redirect('teammates')
    else:
        form = ConnectTeammatesForm()
        return render(request, 'neoapp/assign_teammates.html', {'form': form})