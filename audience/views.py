from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import csv

# Create your views here.
def homepage(request):
    data = {
        "Arsenal": {
            "rank": 1
        },
        "Aston Villa": {
            "rank": 2
        }
    }
    context = {"page": "homepage", "detail": "show all team", "data": data}
    return render(request, "audience/homepage.html", context)

def team_detail(request, team_id):
    data = {
        "team": team_id,
        "team_name": "Arsenal",
        "rank": 1,
        "win": 10,
        "Draw": 10,
        "Player": [
            {
                "player_code": "A",
                "number": 10,
                "goal": 10,
                "match": 10
            },
            {
                "player_code": "US",
                "number": 1,
                "goal": 10,
                "match": 10
            }
        ]
    }
    context = {"page": "team_detail", "detail": f"show detail on each team(team_id ={team_id}).", "data": data}
    return render(request, "audience/team_detail.html", context)

def player_information(request,player_id):
    data = {}
    filename = "audience/static/audience/data/players.csv"
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for r in rows:
            if int(r['Id']) == player_id:
                data = r

    context = {"page": "player_information", "detail": "show all player infos", "data": data}
    return render(request, "audience/player_information.html", context)


