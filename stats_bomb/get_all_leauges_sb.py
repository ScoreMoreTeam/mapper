import json
import os

def get_sb_leauges() -> str:
    result_file_path = "mapper/data/"
    file_path_base = "statsbomb-opendata/open-data/data/"
    folder_matches_path = file_path_base + "matches"

    with open(file_path_base + "competitions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    #Pobranie i zapisanie lig
    competitions_list = [comp for comp in data]
    comps = {str(c['competition_id']): c['competition_name'] for c in competitions_list}
    leauges_file = os.path.join(result_file_path, f"leauges.json")
    print(comps)

    os.makedirs(os.path.dirname(leauges_file), exist_ok=True)
    with open(leauges_file, "w", encoding="utf-8") as f:
        json.dump(comps, f, ensure_ascii=False, indent=4)

    return leauges_file