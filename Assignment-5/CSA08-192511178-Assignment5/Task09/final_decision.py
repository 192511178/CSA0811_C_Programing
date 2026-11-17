"""Task B4: sentiment agreement scaffold and index benchmark."""
import sqlite3, time
from Task05.complaint_ai import label

def main():
    complaints=[
      "Roads are clean and the bus was fast.",
      "Smoke from the factory, air is bad.",
      "The staff were not helpful.",
      "Not bad, service improved."
    ]
    for c in complaints: print(label(c), "|", c)
    con=sqlite3.connect(":memory:")
    con.execute("CREATE TABLE readings(station_id INTEGER, reading_date TEXT, pm25 REAL)")
    con.executemany("INSERT INTO readings VALUES(?,?,?)",
                    [(1,"2026-10-01",48.0),(1,"2026-10-02",50.0),(2,"2026-10-01",95.0)])
    query="SELECT AVG(pm25) FROM readings WHERE station_id=? AND reading_date>=?"
    start=time.perf_counter(); print("Average:",con.execute(query,(1,"2026-10-01")).fetchone())
    print("Before index seconds:",time.perf_counter()-start)
    con.execute("CREATE INDEX idx_station_day ON readings(station_id,reading_date)")
    start=time.perf_counter(); print("Average:",con.execute(query,(1,"2026-10-01")).fetchone())
    print("After index seconds:",time.perf_counter()-start)
    con.close()
    print("Production decision: CSV acquisition, Python cleaning, indexed relational DB, SQL aggregation,")
    print("Pandas analysis, Matplotlib charts; evaluate trained NLP for production complaint volumes.")

if __name__=="__main__": main()
