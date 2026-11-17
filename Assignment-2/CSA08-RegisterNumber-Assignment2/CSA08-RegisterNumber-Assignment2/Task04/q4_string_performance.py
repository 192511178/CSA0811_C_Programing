"""Q4: Compare +=, list+join, and f-string line generation."""
import time
import csv

def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

def build_fstring(records):
    # f-string formats each record; join combines the completed lines.
    lines = [f"{item}" for item in records]
    return "\n".join(lines)

def measure(function, data, repeats=3):
    timings = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(data)
        elapsed = time.perf_counter() - start
        timings.append(elapsed)
        assert isinstance(result, str)
    return timings, sum(timings) / len(timings)

def main():
    rows = []
    for count in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(count)]
        print(f"\nNumber of lines: {count}")
        for name, func in (("plus", build_plus), ("join", build_join), ("fstring_lines", build_fstring)):
            trials, average = measure(func, items)
            print(f"{name:15} trials={['%.6f' % x for x in trials]} average={average:.6f}s")
            rows.append([count, name, *trials, average])
    with open("performance_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["lines", "method", "trial1_seconds", "trial2_seconds", "trial3_seconds", "average_seconds"])
        writer.writerows(rows)
    print("\nSaved performance_results.csv in the current working directory.")

if __name__ == "__main__":
    main()
