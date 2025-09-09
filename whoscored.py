import json
import os
from typing import List
import soccerdata as sd

def init_client() -> sd.WhoScored:
    return sd.WhoScored(leagues= 'ESP-La Liga', seasons= 2021)

def get_whoscored_teams() -> List[str]:
    whoscored = init_client()

    schedule = whoscored.read_schedule()
    teams = schedule["home_team"].drop_duplicates().sort_values().tolist()
    return teams


def get_whoscored_leauges():
    bref = init_client()
    seasons = bref.read_leagues()
    print(seasons.head())  # podgląd kolumn

def get_whoscored_players() -> list[str]:
    whoscored = init_client()
    players_df = whoscored.read_player_season_stats(stat_type="standard")
    players_list = players_df.index.get_level_values("player").unique().tolist()
    return players_list

