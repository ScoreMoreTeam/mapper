
#Pobieramy wszystkie ligi i zapisujemy do pliku
from mapper.combine_dicts import combine_dict_values
from mapper.stats_bomb.get_all_leauges_sb  import get_sb_leauges
from mapper.fbref import get_fbref_leauges, get_fbref_teams, get_fbref_players
from mapper.stats_bomb.get_players_teams_statsbomb import get_sb_players_teams
from mapper.whoscored import get_whoscored_teams



# #---------------------------------------------#
# #-----------------stats_bomb------------------#
# #---------------------------------------------#
leauges_file_path = get_sb_leauges()
print(leauges_file_path)
teams_file, players_file = get_sb_players_teams()

# #---------------------------------------------#
# #--------------------FBref--------------------#
# #---------------------------------------------#
teams = get_fbref_teams()
teams_file_combined_file = "teams_combined.json"
teams_mot_found_file = "teams_not_found.json"
combine_dict_values(teams_file, teams, teams_file_combined_file,teams_mot_found_file)

players_fbref = get_fbref_players()
players_combined_file = "players_combined.json"
players_not_found_file = "players_not_found.json"
combine_dict_values(players_file, players_fbref, players_combined_file, players_not_found_file)

# #---------------------------------------------#
# #------------------WhoScored------------------#
# #---------------------------------------------#
teams_whoscored = get_whoscored_teams()
print(teams_whoscored)
combine_dict_values(teams_file_combined_file, teams_whoscored, teams_file_combined_file, teams_mot_found_file)

