"""
EoC Scraper abstract base class.
All scrapers must use only English and return store-validated, non-invented data.
"""
class BaseScraper:
    def run(self):
        """
        Returns: List of dicts matching:
        {
          "game_name": str,
          "developer": str or None,
          "genre": str or None,
          "update_title": str or None,
          "update_date": str or None,
          "update_content": str or None,
          "levels_added": int or None,
          "source": str
        }
        """
        raise NotImplementedError

ALL_SCRAPERS = []