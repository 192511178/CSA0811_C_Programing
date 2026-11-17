"""Task A3: SQL daily summary and charts. Uses sample data if DB exists."""
import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "Task01" / "air_quality.db"
OUT = Path(__file__).resolve().parent

def main():
    if not DB.exists():
        print("Run Task01/data_acquisition.py first."); return
    con = sqlite3.connect(DB)
    rows = con.execute("""
      SELECT s.station_name, r.reading_date, MIN(r.pm25), MAX(r.pm25),
             AVG(r.pm25), COUNT(r.pm25)
      FROM readings r JOIN stations s USING(station_id)
      GROUP BY s.station_name, r.reading_date
      ORDER BY r.reading_date, s.station_name
    """).fetchall()
    print("Daily summary:", rows)
    data = con.execute("""
      SELECT s.station_name, r.reading_date, r.pm25, r.temperature, r.hour
      FROM readings r JOIN stations s USING(station_id)
      WHERE r.pm25 IS NOT NULL
    """).fetchall()
    con.close()
    if not data:
        print("No valid readings to plot."); return
    # Station comparison
    names = sorted(set(r[0] for r in data))
    means = [sum(r[2] for r in data if r[0] == name) /
             sum(1 for r in data if r[0] == name) for name in names]
    plt.figure(); plt.bar(names, means); plt.xlabel("Station"); plt.ylabel("Mean PM2.5")
    plt.title("Station comparison"); plt.tight_layout(); plt.savefig(OUT/"station_comparison.png")
    # PM2.5 over dates
    dates = sorted(set(r[1] for r in data))
    daily = [sum(r[2] for r in data if r[1] == d)/sum(1 for r in data if r[1] == d) for d in dates]
    plt.figure(); plt.plot(dates, daily, marker="o"); plt.xlabel("Date"); plt.ylabel("Mean PM2.5")
    plt.title("PM2.5 trend"); plt.xticks(rotation=30); plt.tight_layout(); plt.savefig(OUT/"pm25_trend.png")
    # Temperature scatter
    scatter = [(r[3],r[2]) for r in data if r[3] is not None]
    if scatter:
        plt.figure(); plt.scatter([x[0] for x in scatter],[x[1] for x in scatter])
        plt.xlabel("Temperature (C)"); plt.ylabel("PM2.5"); plt.title("Temperature vs PM2.5")
        plt.tight_layout(); plt.savefig(OUT/"temperature_scatter.png")
    print("Charts saved in", OUT)

if __name__ == "__main__": main()
