import json
import os


def get_sb_players_teams():
    result_file_path = "mapper/data/"
    file_path_base = "statsbomb-opendata/open-data/data/"
    folder_matches_path = file_path_base + "matches"

    with open(file_path_base + "competitions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    #Wartosci do zmiany
    leauge_name = "La Liga" 
    season = "2020/2021"
    competitions_list = [comp for comp in data if comp["season_name"] == season and comp["competition_name"] == leauge_name]

    competition = competitions_list[0]
    print("competition")
    print(competition)

    competiton_matches_season_folder = folder_matches_path + "/" + str(competition["competition_id"]) + "/" + str(competition["season_id"])
    with open(competiton_matches_season_folder + ".json", "r", encoding="utf-8") as f:
        data = json.load(f)
    match_ids = [match["match_id"] for match in data]

    lineups_path = file_path_base + "/lineups/"
    teams = {}
    players = {}
    for match_id in match_ids:
        with open(f"{lineups_path}{match_id}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for team in data:
                teams[team["team_id"]] = team["team_name"]
                for player in team["lineup"]:
                    players[player["player_id"]] = player["player_name"] 


    teams_file = os.path.join(result_file_path, f"teams_{leauge_name}.json")
    players_file = os.path.join(result_file_path, f"players_{leauge_name}.json")

    os.makedirs(os.path.dirname(teams_file), exist_ok=True)
    os.makedirs(os.path.dirname(players_file), exist_ok=True)

    with open(teams_file, "w", encoding="utf-8") as f:
        json.dump(teams, f, ensure_ascii=False, indent=4)

    with open(players_file, "w", encoding="utf-8") as f:
        json.dump(players, f, ensure_ascii=False, indent=4)

    print(f"Zapisano {len(teams)} drużyn do {teams_file}")
    print(f"Zapisano {len(players)} zawodników do {players_file}")
    return teams_file, players_file