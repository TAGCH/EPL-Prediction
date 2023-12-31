from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('team_detail/<int:team_id>', views.team_detail, name="team_detail"),
    path('team_comparison/', views.team_comparison, name='team_comparison'),
    path('player_information/<str:team_name>/<int:player_id>', views.player_information, name="player_information"),
]
