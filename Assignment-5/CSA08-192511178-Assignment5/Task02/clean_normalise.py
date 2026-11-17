"""Task A2: cleaning rules and normalisation examples."""
from statistics import median, mean, pstdev

def clean_values(values):
    valid = []
    for value in values:
        if value is None or str(value).strip().upper() in ("", "NA"):
            continue
        try: number = float(value)
        except (TypeError, ValueError): continue
        if 0 <= number <= 999: valid.append(number)
    return valid

def min_max(values):
    if not values: return []
    lo, hi = min(values), max(values)
    return [0.0 for _ in values] if lo == hi else [round((x-lo)/(hi-lo), 3) for x in values]

def z_score(values):
    if not values: return []
    sd = pstdev(values)
    return [0.0 for _ in values] if sd == 0 else [(x-mean(values))/sd for x in values]

def fahrenheit_to_celsius(value):
    return (float(value)-32)*5/9

if __name__ == "__main__":
    raw = [48, "NA", "", -5, 95, 121, 1200, "oops"]
    cleaned = clean_values(raw)
    print("Cleaned:", cleaned)
    print("Min-max:", min_max(cleaned))
    print("Z-score:", [round(x,3) for x in z_score(cleaned)])
    print("86 F in C:", round(fahrenheit_to_celsius(86), 2))
