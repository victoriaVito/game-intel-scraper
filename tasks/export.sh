#!/bin/bash
# Export data from game-intel-scraper
# Usage: ./export.sh [format]
format=${1:-csv}
python3 main.py export --format $format
