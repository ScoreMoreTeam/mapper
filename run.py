import utils as utils
import fbref
import soccerdata as sd
import whoscored
import statsBomb

leauge = 'ESP-La Liga'
season = 2021

# #---------------------------------------------#
# #-----------------stats_bomb------------------#
# #---------------------------------------------#
leauges_file_path = statsBomb.get_leauges()
print(leauges_file_path)
teams_file, players_file = statsBomb.get_players_teams("La Liga", "2020/2021")

# # #---------------------------------------------#
# # #--------------------FBref--------------------#
# # #---------------------------------------------#
fbref_client = sd.FBref(leagues= leauge, seasons= season)
teams = fbref.get_teams(fbref_client, leauge, season)
players_fbref = fbref.get_fbref_players(fbref_client, leauge, season)


# # #---------------------------------------------#
# # #------------------WhoScored------------------#
# # #---------------------------------------------#
# whoscored_client = sd.WhoScored(leagues= leauge, seasons= season)
# teams_whoscored = whoscored.get_whoscored_teams(whoscored_client, leauge, season)


