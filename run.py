import os
import utils as utils
import fbref
import soccerdata as sd
import whoscored
import statsBomb
import utils

league = 'ESP-La Liga'
season = 2021

# Foldery i pliki
os.makedirs(f"data/json/{league}/{season}/combined", exist_ok=True)

combined_teams_file = f"data/json/combined/{league}/teams.json"
combined_players_file = f"data/json/combined/{league}/players.json"
players_not_combined_file = f"data/json/combined/{league}/players_not_combined_file.json"
teams_not_combined_file = f"data/json/combined/{league}/teams_not_combined_file.json"


# #---------------------------------------------#
# #-----------------stats_bomb------------------#
# #---------------------------------------------#
leauges_file_path = statsBomb.get_leauges()
teams_file, players_file = statsBomb.get_players_teams("La Liga", "2020/2021")

# # #---------------------------------------------#
# # #--------------------FBref--------------------#
# # #---------------------------------------------#
fbref_client = sd.FBref(leagues= league, seasons= season)
teams_fbref = fbref.get_teams(fbref_client, league, season)
players_fbref = fbref.get_fbref_players(fbref_client, league, season)
utils.combine_dict_values(teams_file, teams_fbref, combined_teams_file, teams_not_combined_file)
utils.combine_dict_values(players_file, players_fbref, combined_players_file, players_not_combined_file)

print(teams_not_combined_file)

# # #---------------------------------------------#
# # #------------------WhoScored------------------#
# # #---------------------------------------------#
whoscored_client = sd.WhoScored(leagues= league, seasons= season)
teams_whoscored = whoscored.get_whoscored_teams(whoscored_client, league, season)
utils.combine_dict_values(combined_teams_file, teams_whoscored, combined_teams_file, teams_not_combined_file)


