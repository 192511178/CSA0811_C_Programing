"""Q5: Clean sensor readings using loops, comprehensions, map/filter and enumerate."""
import random, time, sys, csv

def loop_version(readings):
    valid_c = []
    for value in readings:
        if -50 <= value <= 50:
            valid_c.append(value)
    valid_f = []
    for value in valid_c:
        valid_f.append(value * 9 / 5 + 32)
    alarms = [i for i, value in enumerate(readings) if -50 <= value <= 50 and not (2 <= value <= 8)]
    return valid_c, valid_f, alarms

def comprehension_version(readings):
    valid_c = [v for v in readings if -50 <= v <= 50]
    valid_f = [v * 9 / 5 + 32 for v in valid_c]
    alarms = [i for i, v in enumerate(readings) if -50 <= v <= 50 and not (2 <= v <= 8)]
    return valid_c, valid_f, alarms

def map_filter_version(readings):
    valid_c = list(filter(lambda v: -50 <= v <= 50, readings))
    valid_f = list(map(lambda v: v * 9 / 5 + 32, valid_c))
    alarms = [i for i, v in enumerate(readings) if -50 <= v <= 50 and not (2 <= v <= 8)]
    return valid_c, valid_f, alarms

def benchmark():
    rows = []
    for n in (10_000, 100_000, 1_000_000):
        readings = [random.uniform(-60, 60) for _ in range(n)]
        results = []
        for name, func in (("loop", loop_version), ("comprehension", comprehension_version), ("map_filter", map_filter_version)):
            start = time.perf_counter(); result = func(readings); elapsed = time.perf_counter() - start
            results.append(result)
            print(f"n={n} {name}: {elapsed:.6f}s")
            rows.append([n, name, elapsed])
        assert results[0] == results[1] == results[2]
    sample = [4, 9, 55, -55, 6]
    list_comp = [x for x in sample if -50 <= x <= 50]
    gen = (x for x in sample if -50 <= x <= 50)
    print("List comprehension size:", sys.getsizeof(list_comp))
    print("Generator object size:", sys.getsizeof(gen))
    with open("q5_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["readings", "method", "seconds"]); w.writerows(rows)

def main():
    sample = [4, 9, 55, -55, 6, 2, 8]
    print("Loop:", loop_version(sample))
    print("Comprehension:", comprehension_version(sample))
    print("Map/filter:", map_filter_version(sample))
    print("All-valid:", comprehension_version([3, 4, 5]))
    print("All-invalid:", comprehension_version([60, -70]))
    benchmark()

if __name__ == "__main__":
    main()
