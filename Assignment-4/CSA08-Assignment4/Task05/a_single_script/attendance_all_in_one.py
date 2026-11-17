"""Task 5(a): Single-script organisation."""
def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip().split(",") for line in f if line.strip()]

def percentage(present, total):
    return 0 if total == 0 else present / total * 100

def write_report(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(",".join(map(str, row)) + "\n")

if __name__ == "__main__":
    print("Single-script attendance utility")
