"""
Handles all DB operations for EoC using SQLite.
All DB inserts/reads must enforce English+official validation.
"""
import sqlite3
import os

DB_PATH = "db/games.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def get_all_games():
    conn = get_conn()
    games = []
    try:
        cursor = conn.execute("SELECT * FROM games WHERE verified=1;")
        cols = [desc[0] for desc in cursor.description]
        for row in cursor:
            games.append(dict(zip(cols, row)))
    except Exception:
        pass
    conn.close()
    return games

def get_all_updates():
    conn = get_conn()
    updates = []
    try:
        cursor = conn.execute("SELECT * FROM updates WHERE verified=1;")
        cols = [desc[0] for desc in cursor.description]
        for row in cursor:
            updates.append(dict(zip(cols, row)))
    except Exception:
        pass
    conn.close()
    return updates

def save_game_update(r):
    conn = get_conn()
    c = conn.cursor()
    # Save only basic fields for example.
    c.execute(
        "INSERT OR IGNORE INTO games (name, developer, genre, verified, source) VALUES (?, ?, ?, ?, ?)",
        (r.get("game_name"), r.get("developer"), r.get("genre"), r.get("verified", 0), r.get("source"))
    )
    conn.commit()
    conn.close()