import json
from typing import List
import soccerdata as sd

def init_client() -> sd.FBref:
    return sd.FBref(leagues= 'ESP-La Liga', seasons= 2021)

def get_fbref_teams() -> List[str]:
    fbref = init_client()

    seasons = fbref.read_team_season_stats()
    seasons_reset = seasons.reset_index()
    teams = seasons_reset['team'].unique()
    print(teams)
    return teams

def get_fbref_leauges():
    bref = init_client()
    seasons = bref.read_leagues()
    print(seasons.head())  # podgląd kolumn

def get_fbref_players() -> list[str]:
    bref = init_client()
    players_df = bref.read_player_season_stats(stat_type="standard")
    players_list = players_df.index.get_level_values("player").unique().tolist()
    return players_list

