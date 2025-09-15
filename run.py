import utils as utils
import statsBomb
import fbref
import whoscored
import soccerdata as sd

leauge = 'ESP-La Liga'
season = 2021

# #---------------------------------------------#
# #-----------------stats_bomb------------------#
# #---------------------------------------------#
# leauges_file_path = statsBomb.get_leauges()
# print(leauges_file_path)
# teams_file, players_file = statsBomb.get_players_teams()

# #---------------------------------------------#
# #--------------------FBref--------------------#
# #---------------------------------------------#
fbref_client = sd.FBref(leagues= leauge, seasons= season)
teams = fbref.get_teams(fbref_client)
players_fbref = fbref.get_fbref_players(fbref_client)


# #---------------------------------------------#
# #------------------WhoScored------------------#
# #---------------------------------------------#
# whoscored_client = sd.WhoScored(leagues= leauge, seasons= season)
# teams_whoscored = whoscored_client.get_whoscored_teams(whoscored_client)


