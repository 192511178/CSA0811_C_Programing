"""Task B1: complete CSV cleaning and min-max normalisation."""
import csv, io
RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""
def load_clean(text):
    rows=[]
    for row in csv.DictReader(io.StringIO(text)):
        value=row.get("pm25","").strip()
        if not value or value.upper()=="NA": continue
        try: pm=float(value)
        except ValueError: continue
        if pm < 0 or pm > 999: continue
        rows.append((row["station"],row["date"],pm))
    return rows
def min_max(values):
    if not values: return []
    lo,hi=min(values),max(values)
    if lo==hi: return [0.0 for _ in values]
    return [round((v-lo)/(hi-lo),3) for v in values]
if __name__=="__main__":
    clean=load_clean(RAW)
    print(clean)
    print(min_max([pm for _,_,pm in clean]))
