"""
Scaffold for running all the scrapers for EoC.
All execution is English-only and validated with official stores.
No invented or guessed data is permitted.
"""
from scrapers.base_scraper import ALL_SCRAPERS
from src.store_validator import is_verified
from src.db_manager import save_game_update

def run_all_scrapers():
    print("Running all EoC game scrapers...")
    for scraper in ALL_SCRAPERS:
        try:
            print(f"Scraping with {scraper.__class__.__name__} ...")
            results = scraper().run()
            for r in results:
                verified, report = is_verified(r)
                r["verified"] = verified
                r["validation_report"] = report
                if verified:
                    save_game_update(r)
        except Exception as e:
            print(f"Error: {e}")