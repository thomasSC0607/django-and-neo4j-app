from django import forms
from .models import Player, Team, Coach

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    height = forms.FloatField()
    number = forms.IntegerField()
    weight = forms.IntegerField()

class TeamForm(forms.Form):
    name = forms.CharField(max_length=100)

class CoachForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

class AssignPlayerToTeamForm(forms.Form):
    player = forms.ChoiceField(choices=[])
    team = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].choices = [(p.name, p.name) for p in Player.nodes.all()]
        self.fields['team'].choices = [(t.name, t.name) for t in Team.nodes.all()]

class AssignCoachToPlayer(forms.Form):
    coach = forms.ChoiceField(choices=[])
    player = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coach'].choices = [(c.name, c.name) for c in Coach.nodes.all()]
        self.fields['player'].choices = [(p.name, p.name) for p in Player.nodes.all()]

class AssignCoachToTeamForm(forms.Form):
    coach = forms.ChoiceField(choices=[])
    team = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coach'].choices = [(c.name, c.name) for c in Coach.nodes.all()]
        self.fields['team'].choices = [(t.name, t.name) for t in Team.nodes.all()]

class ConnectTeammatesForm(forms.Form):
    player1 = forms.ChoiceField(choices=[])
    player2 = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player1'].choices = [(p.name, p.name) for p in Player.nodes.all()]
        self.fields['player2'].choices = [(p.name, p.name) for p in Player.nodes.all()]