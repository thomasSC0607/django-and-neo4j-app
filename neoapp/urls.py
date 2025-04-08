from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('players/', views.player_list, name='player_list'),
    path('add_player/', views.add_player, name='add_player'),
    path('teams/', views.team_list, name='team_list'),
    path('add_team/', views.add_team, name='add_team'),
    path('coaches/', views.coach_list, name='coach_list'),
    path('add_coach/', views.add_coach, name='add_coach'),
    path('player_to_team/', views.assign_player_to_team, name='player_to_team'),
    path('coach_to_player/', views.assign_coach_to_player, name='coach_to_player'),
    path('coach_to_team/', views.assign_coach_to_team, name='coach_to_team'),
    path('teammates/', views.ConnectTeammates, name='teammates'),
]