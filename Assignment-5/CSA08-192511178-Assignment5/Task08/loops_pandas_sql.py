"""Task B3: compare Python, Pandas and SQLite daily means."""
import csv, sqlite3, time
from pathlib import Path

DATA=[("Adyar","2026-10-01",48.0),("Adyar","2026-10-01",60.0),
      ("Guindy","2026-10-01",95.0),("Guindy","2026-10-01",121.0)]

def loops(rows):
    agg={}
    for station,day,value in rows:
        key=(station,day)
        total,count=agg.get(key,(0.0,0))
        agg[key]=(total+value,count+1)
    return {k:v[0]/v[1] for k,v in agg.items()}

def main():
    print("Python:",loops(DATA))
    try:
        import pandas as pd
        df=pd.DataFrame(DATA,columns=["station","day","pm25"])
        print("Pandas:",df.groupby(["station","day"])["pm25"].mean().to_dict())
    except ImportError:
        print("Pandas not installed; install requirements.txt")
    con=sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES(?,?,?)",DATA)
    print("SQL:",con.execute("SELECT station,day,AVG(pm25) FROM aq GROUP BY station,day").fetchall())
    con.close()
    start=time.perf_counter(); loops(DATA); print("Loop seconds:",time.perf_counter()-start)
if __name__=="__main__": main()
