from difflib import get_close_matches
import json
import os
from typing import Dict, List


def combine_dict_values(base_dict_path: str, values_list: List[str], final_dict_path: str, not_combined_path: str) -> str:
    """
    Dla każdego elementu z values_list:
    1. Szuka pełnego dopasowania w wartościach słownika (case-insensitive).
    2. Jeśli nie znajdzie, a wartość zawiera co najmniej dwa słowa -> sprawdza czy
       zarówno pierwsze, jak i ostatnie słowo znajdują się w wartości słownika.
    3. Jeśli znajdzie dopasowanie, dopisuje element do wartości (bez duplikatu).
    4. Wypisuje elementy, dla których nie znaleziono dopasowania.
    """

    # Wczytanie bazowego słownika
    with open(base_dict_path, "r", encoding="utf-8") as f:
        base_dict = json.load(f)

    not_combined_values = set()

    for value in values_list:
        value_lower = value.lower()
        words = value.split()
        found = False

        # 1️⃣ Sprawdzenie pełnej frazy
        for key in base_dict:
            if value_lower in base_dict[key].lower():
                existing_values = [v.lower() for v in base_dict[key].split(",")]
                if value_lower not in existing_values:
                    base_dict[key] = f"{base_dict[key]},{value}"
                found = True
                break

        # 2️⃣ Sprawdzenie pierwszego i ostatniego słowa (jeśli są co najmniej dwa słowa)
        if not found and len(words) > 1:
            first_word = words[0].lower()
            last_word = words[-1].lower()
            for key in base_dict:
                key_values_lower = base_dict[key].lower()
                if first_word in key_values_lower and last_word in key_values_lower:
                    existing_values = [v.lower() for v in base_dict[key].split(",")]
                    if value_lower not in existing_values:
                        base_dict[key] = f"{base_dict[key]},{value}"
                    found = True
                    break

        # 3️⃣ Wypisanie nieznalezionych wartości
        if not found:
            not_combined_values.add(value)
            print(f"Nie znaleziono dopasowania dla wartości: {value}")

    # 4️⃣ Zapis do pliku
    if final_dict_path:
        with open(final_dict_path, "w", encoding="utf-8") as f:
            json.dump(base_dict, f, ensure_ascii=False, indent=4)

    # 5️⃣ Dopisywanie do not_combined_path
    if not_combined_values and not_combined_path:
        directory = os.path.dirname(not_combined_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        existing_not_combined = set()
        if os.path.exists(not_combined_path):
            with open(not_combined_path, "r", encoding="utf-8") as f:
                existing_not_combined = set(json.load(f))

        combined_not_found = list(existing_not_combined.union(not_combined_values))
        with open(not_combined_path, "w", encoding="utf-8") as f:
            json.dump(combined_not_found, f, ensure_ascii=False, indent=4)

    return final_dict_path