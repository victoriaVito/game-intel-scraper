import sys
from src.top_games import run_all_scrapers
from src.export_manager import export_csv, export_json, export_sqlite, export_mongo, export_indexdb

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [scrape|export|dashboard]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "scrape":
        run_all_scrapers()
    elif cmd == "export":
        fmt = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--format" else "csv"
        if fmt == "csv":
            export_csv()
        elif fmt == "json":
            export_json()
        elif fmt == "sqlite":
            export_sqlite()
        elif fmt == "mongo":
            export_mongo()
        elif fmt == "indexdb":
            export_indexdb()
        else:
            print("Unknown format")
    elif cmd == "dashboard":
        from src.dashboard import app
        app.main()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()