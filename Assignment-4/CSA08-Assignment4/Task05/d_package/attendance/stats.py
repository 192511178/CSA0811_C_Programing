def percentage(present, total):
    return 0 if total == 0 else present / total * 100

def below_threshold(records, threshold=75):
    return [r for r in records if percentage(r["present"], r["total"]) < threshold]
