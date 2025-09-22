import json
from pathlib import Path
import time
from typing import List
import pandas as pd
import soccerdata as sd

def get_whoscored_teams(whoscored: sd.WhoScored, leauge: str, season: str) -> List[str]:
    schedule = whoscored.read_schedule()

    Path(f"data/csv/{leauge}/{season}/whoscored").mkdir(parents=True, exist_ok=True)

    schedule = schedule.reset_index()
    schedule.to_csv(f"data/csv/{leauge}/{season}/whoscored/teams.csv", index=False)

    Path(f"data/json/{leauge}/{season}/whoscored").mkdir(parents=True, exist_ok=True)
    teams = (
        schedule[["home_team", "home_team_id"]]
            .drop_duplicates()
            .sort_values(by="home_team")
            .rename(columns={"home_team_id": "id",  "home_team": "name"})       
    )
    teams.to_json(f'data/json/{leauge}/{season}/whoscored/teams.json', orient='records', force_ascii=False, indent=4)

    return teams.to_dict(orient="records")