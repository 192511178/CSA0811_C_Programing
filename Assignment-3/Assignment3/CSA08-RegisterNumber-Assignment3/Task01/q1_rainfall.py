"""Q1: Daily rainfall records - weekly totals, extrema, moving averages and experiments."""
import random, time, csv

def weekly_totals(readings):
    return [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]

def naive_moving_average(readings, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    if len(readings) < window:
        return []
    return [sum(readings[i:i+window]) / window for i in range(len(readings)-window+1)]

def running_moving_average(readings, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    if len(readings) < window:
        return []
    current = sum(readings[:window])
    result = [current / window]
    for i in range(window, len(readings)):
        current += readings[i] - readings[i-window]
        result.append(current / window)
    return result

def analyse(readings):
    if not readings:
        return {"weekly_totals": [], "max": None, "min": None,
                "moving_average": [], "dry_days": []}
    return {
        "weekly_totals": weekly_totals(readings),
        "max": (max(readings), readings.index(max(readings))),
        "min": (min(readings), readings.index(min(readings))),
        "moving_average": running_moving_average(readings),
        "dry_days": [i+1 for i, value in enumerate(readings) if value == 0],
    }

def experiment():
    rows = []
    for n in (365, 36_500, 365_000):
        data = [random.randint(0, 100) for _ in range(n)]
        for name, func in (("naive", naive_moving_average), ("running_sum", running_moving_average)):
            start = time.perf_counter()
            result = func(data)
            elapsed = time.perf_counter() - start
            rows.append([n, name, elapsed, len(result)])
            print(f"n={n:>7} {name:12} time={elapsed:.6f}s outputs={len(result)}")
    with open("q1_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["readings", "method", "seconds", "output_count"]); w.writerows(rows)

def main():
    sample = [0, 5, 8, 0, 12, 3, 7, 4, 0, 2, 6, 9, 1, 0]
    print("Sample readings:", sample)
    print("Weekly totals:", weekly_totals(sample))
    print("Wettest (value, zero-based position):", max((v, i) for i, v in enumerate(sample)))
    print("Driest (value, zero-based position):", min((v, i) for i, v in enumerate(sample)))
    print("7-day moving average:", running_moving_average(sample))
    print("Dry days (1-based day numbers):", [i+1 for i, v in enumerate(sample) if v == 0])
    print("Empty list moving average:", running_moving_average([]))
    print("Short list moving average:", running_moving_average([1, 2, 3]))
    experiment()

if __name__ == "__main__":
    main()
