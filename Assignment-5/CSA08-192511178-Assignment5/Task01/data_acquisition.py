"""Task A1: inspect CSV source and create SQLite schema."""
import csv, sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV_FILE = HERE / "sample_station.csv"
DB_FILE = HERE / "air_quality.db"

def create_sample():
    if not CSV_FILE.exists():
        CSV_FILE.write_text(
            "station,date,hour,pm25,pm10,no2,temperature\n"
            "Adyar,2026-10-01,01:00,48,80,24,29\n"
            "Adyar,2026-10-01,02:00,NA,75,21,30\n"
            "Guindy,2026-10-01,01:00,95,120,35,31\n", encoding="utf-8"
        )

def main():
    create_sample()
    con = sqlite3.connect(DB_FILE)
    con.executescript("""
    PRAGMA foreign_keys = ON;
    CREATE TABLE IF NOT EXISTS stations(
      station_id INTEGER PRIMARY KEY,
      station_name TEXT UNIQUE NOT NULL,
      temperature_unit TEXT NOT NULL CHECK(temperature_unit IN ('C','F'))
    );
    CREATE TABLE IF NOT EXISTS readings(
      station_id INTEGER NOT NULL,
      reading_date TEXT NOT NULL,
      hour TEXT NOT NULL,
      pm25 REAL, pm10 REAL, no2 REAL, temperature REAL,
      PRIMARY KEY(station_id, reading_date, hour),
      FOREIGN KEY(station_id) REFERENCES stations(station_id)
    );
    """)
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            unit = "C"
            con.execute("INSERT OR IGNORE INTO stations(station_name,temperature_unit) VALUES (?,?)",
                        (row["station"].strip().title(), unit))
            sid = con.execute("SELECT station_id FROM stations WHERE station_name=?",
                              (row["station"].strip().title(),)).fetchone()[0]
            def number(v):
                try: return float(v) if v.strip().upper() not in ("", "NA") else None
                except ValueError: return None
            con.execute("""INSERT OR REPLACE INTO readings
              VALUES(?,?,?,?,?,?,?)""",
              (sid,row["date"],row["hour"],number(row["pm25"]),number(row["pm10"]),
               number(row["no2"]),number(row["temperature"])))
    con.commit()
    print("Database created:", DB_FILE)
    print("Readings:", con.execute("SELECT COUNT(*) FROM readings").fetchone()[0])
    con.close()

if __name__ == "__main__": main()
