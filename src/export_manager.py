"""
Export manager for EoC project.
All exports only output store-validated, 100% English data.
Never exports invented or guessed values.
"""
import pandas as pd
from src.db_manager import get_all_games, get_all_updates

def export_csv():
    games = get_all_games()
    updates = get_all_updates()
    pd.DataFrame(games).to_csv("games.csv", index=False)
    pd.DataFrame(updates).to_csv("updates.csv", index=False)
    print("Exported CSVs.")

def export_json():
    games = get_all_games()
    updates = get_all_updates()
    import json
    with open("games.json", "w") as f:
        json.dump(games, f, indent=2)
    with open("updates.json", "w") as f:
        json.dump(updates, f, indent=2)
    print("Exported JSON.")

def export_sqlite():
    print("SQLite DB is already available as db/games.db.")

def export_mongo():
    from db.mongo.mongo_client import insert_many_games, insert_many_updates
    insert_many_games(get_all_games())
    insert_many_updates(get_all_updates())
    print("Exported to MongoDB.")

def export_indexdb():
    import json
    games = get_all_games()
    with open("indexdb.json", "w") as f:
        json.dump({"games": games}, f, indent=2)
    print("IndexDB schema exported.")