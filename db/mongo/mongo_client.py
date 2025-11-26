"""
MongoDB client for EoC.
All data writes must be English, validated, and never invented.
"""
from pymongo import MongoClient

def get_client():
    return MongoClient("mongodb://localhost:27017/")

def insert_many_games(games):
    if not games:
        return
    db = get_client().eoc_db
    db.games.insert_many(games)

def insert_many_updates(updates):
    if not updates:
        return
    db = get_client().eoc_db
    db.updates.insert_many(updates)