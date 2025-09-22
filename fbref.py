import json
from pathlib import Path
from typing import List
import soccerdata as sd

def get_teams(fbref: sd.FBref, leauge: str, season:str) -> List[str]:
    seasons = fbref.read_team_season_stats()
    # Utwórz folder, jeśli nie istnieje
    Path(f"data/csv/{leauge}/{season}/fbref").mkdir(parents=True, exist_ok=True)

    seasons_reset = seasons.reset_index()
    seasons_reset.to_csv(f"data/csv/{leauge}/{season}/fbref/teams.csv", index=False)

    # Przykład DataFrame
    teams = seasons_reset[['team', 'url']].drop_duplicates().rename(columns={"team": "name"})

    # Wyciągamy ID drużyny z URL
    teams['id'] = teams['url'].apply(lambda x: x.split('/')[3] if len(x.split('/')) > 3 else None)

    # Usuwamy oryginalną kolumnę url
    teams = teams.drop(columns=['url'])
    Path(f"data/json/{leauge}/{season}/fbref").mkdir(parents=True, exist_ok=True)

    teams.columns = [col if isinstance(col, str) else col[0] for col in teams.columns]
    teams.to_json(f'data/json/{leauge}/{season}/fbref/teams.json', orient='records', force_ascii=False, indent=4)

    return teams.to_dict(orient="records")

def get_fbref_players(fbref: sd.FBref, league: str, season:str) -> list[str]:
    players_df = fbref.read_player_season_stats(stat_type="standard")
    players_df.to_csv(f"data/csv/{league}/{season}/fbref/players.csv")
    players_list = players_df.index.get_level_values("player").unique().tolist()

    players_json = [{"id": "", "name": player} for player in players_list]

    with open(f"data/json/{league}/{season}/fbref/players.json", "w", encoding="utf-8") as f:
        json.dump(players_json, f, ensure_ascii=False, indent=4)

    return players_json