"""Task B2: parameterised SQL and adversarial CSV checks."""
import sqlite3, csv, io

readings=[("Adyar","2026-10-01",48.0),("Guindy","2026-10-01",95.0),
          ("Guindy","2026-10-03",121.0),("Adyar","2026-10-04",60.0)]
con=sqlite3.connect(":memory:")
con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
con.executemany("INSERT INTO aq VALUES(?,?,?)",readings)
con.commit()

def station_average(name):
    row=con.execute("SELECT AVG(pm25) FROM aq WHERE station=?",(name,)).fetchone()
    return row[0]

def inspect_csv(text):
    try:
        reader=csv.DictReader(io.StringIO(text))
        required={"station","date","pm25"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            return "Missing required column"
        return f"Rows: {sum(1 for _ in reader)}"
    except (csv.Error, UnicodeError) as exc:
        return f"CSV error: {exc}"

if __name__=="__main__":
    print(station_average("Adyar"),station_average("Guindy"))
    print(station_average("Adyar' OR '1'='1"))
    print(inspect_csv("station,date\\nAdyar,2026-10-01"))
    con.close()
