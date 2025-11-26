# EoC — Official Game Update Intelligence System

## Overview

**EoC** (Evolution of Competitors) is a production-grade, fully automated system for collecting, validating, and analyzing mobile game intelligence.  
Every single datum is validated using official sources: Google Play Store and Apple App Store.  
Absolutely no data is invented, guessed, or inferred. The system and this documentation are 100% in English.

---

## Architecture

```
EoC/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── top_games.py
│   ├── classifier.py
│   ├── updater.py
│   ├── pdf_reader.py
│   ├── db_manager.py
│   ├── export_manager.py
│   ├── store_validator.py
│   └── dashboard/
│       ├── app.py
│       ├── components.py
│       └── charts.py
│
├── scrapers/
│   ├── base_scraper.py
│   ├── allpatchnotes_scraper.py
│   ├── updatecrazy_scraper.py
│   ├── patchtracker_scraper.py
│   ├── gamenotifier_scraper.py
│   ├── apkpure_scraper.py
│   └── ankergames_scraper.py
│
├── parsers/
│   ├── match3_detector.py
│   ├── patch_parser.py
│   ├── release_cycle_parser.py
│   ├── level_update_parser.py
│   └── developer_parser.py
│
├── pdf/
│   ├── pdf_scraper.py
│   └── pdf_table_parser.py
│
├── utils/
│   ├── logger.py
│   ├── helpers.py
│   ├── browser.py
│   ├── validation.py
│   └── store_api.py
│
├── db/
│   ├── games.db
│   ├── seed/
│   ├── migrations/
│   └── mongo/
│       ├── mongo_client.py
│       └── indexdb_schema.json
│
├── prompts/
│   ├── parser_rules.md
│   ├── scraper_rules.md
│   ├── data_quality_rules.md
│   └── classification_rules.md
│
└── .github/
    └── workflows/
        └── daily_scraper.yml
```

---

## Quickstart

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run all scrapers:**
```bash
python main.py scrape
```

**Export data:**
```bash
python main.py export --format csv
python main.py export --format mongo
```

**View dashboard:**
```bash
streamlit run src/dashboard/app.py
```

---

## Official Store Validation

- Every record is checked against both Google Play and Apple App Store.
- If there are discrepancies or missing store data, "verified" is set to false and the record is not saved.
- Official store values override all others. Nothing is guessed or inferred.

---

## Extending with Prompts

Add new KPIs, scrapers, or refactor modules by using templates under `/prompts/`.  
All changes must pass store validation and never synthesize data.

---

## CI/CD

Nightly scraping, validation, and export is automated with GitHub Actions.  
Schedule: Every day at 02:00 UTC.

---

## Data Policy

- No Spanish. No invented or guessed data.
- Everything is strictly checked and English-only.

---
