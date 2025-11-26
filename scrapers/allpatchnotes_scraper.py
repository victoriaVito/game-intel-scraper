"""
Scraper for allpatchnotes.com
Must use Playwright/BS4 as needed.
English-only, never guesses, only outputs after store validation.
"""
from scrapers.base_scraper import BaseScraper

class AllPatchNotesScraper(BaseScraper):
    def run(self):
        return []