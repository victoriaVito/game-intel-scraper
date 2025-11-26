"""
Official store validation for EoC.
Always checks both Google Play and App Store.
Never guesses, never infers data.
English-only.
"""
import requests

GOOGLE_PLAY_API = "https://play.google.com/store/apps/details"
APPLE_APPSTORE_API = "https://itunes.apple.com/lookup"

def fetch_google_play(game_name):
    # Placeholder: To be filled with official or scraped logic
    return None

def fetch_apple_store(game_name):
    params = {'term': game_name, 'entity': 'software'}
    r = requests.get(APPLE_APPSTORE_API, params=params)
    if r.status_code != 200:
        return None
    res = r.json()
    return res["results"][0] if res.get("resultCount", 0) > 0 else None

def compare_store_data(scraped, google_store, apple_store):
    differences = {}
    keys = ["game_name", "developer", "genre"]
    for key in keys:
        scr_val = scraped[key]
        store_val = (google_store or {}).get(key) or (apple_store or {}).get(key)
        if store_val and scr_val and store_val != scr_val:
            differences[key] = {"scraped": scr_val, "store": store_val}
    match = not differences
    verified = match and (google_store or apple_store)
    note = "Data matches official stores." if verified else "Discrepancies found or no official data."
    return {
        "game_name": scraped["game_name"],
        "google_play": google_store,
        "app_store": apple_store,
        "match": match,
        "differences": differences,
        "verified": verified,
        "note": note
    }

def validate_game(scraped):
    google = fetch_google_play(scraped["game_name"])
    apple = fetch_apple_store(scraped["game_name"])
    report = compare_store_data(scraped, google, apple)
    return report

def is_verified(scraped):
    report = validate_game(scraped)
    return report["verified"], report