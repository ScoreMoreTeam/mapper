from typing import List
import soccerdata as sd

def get_whoscored_teams(whoscored: sd.WhoScored) -> List[str]:
    schedule = whoscored.read_schedule()
    teams = schedule["home_team"].drop_duplicates().sort_values().tolist()
    return teams

def get_whoscored_leauges(whoscored: sd.WhoScored):
    seasons = whoscored.read_leagues()
    print(seasons.head())  # podgląd kolumn

def get_whoscored_players(whoscored: sd.WhoScored) -> list[str]:
    players_df = whoscored.read_player_season_stats(stat_type="standard")
    players_list = players_df.index.get_level_values("player").unique().tolist()
    return players_list

