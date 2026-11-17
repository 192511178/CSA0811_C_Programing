"""Q6: Nested railway timetable, station/day queries, sorted departures and index benchmark."""
import random, time, csv, sys

def sample_timetable():
    return {
        "12601": {"name": "Express A", "stops": [("Chennai", "06:00", "06:10"), ("Katpadi", "08:00", "08:05"), ("Bengaluru", "11:00", "11:10")], "days": {"Mon", "Wed", "Fri"}},
        "12602": {"name": "Express B", "stops": [("Chennai", "07:00", "07:15"), ("Salem", "10:00", "10:05"), ("Coimbatore", "12:00", "12:10")], "days": {"Tue", "Thu", "Sat"}},
        "12603": {"name": "Express C", "stops": [("Bengaluru", "05:00", "05:10"), ("Katpadi", "08:30", "08:35"), ("Chennai", "11:30", "11:40")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
        "12604": {"name": "Express D", "stops": [("Chennai", "09:00", "09:10"), ("Villupuram", "11:00", "11:05"), ("Trichy", "14:00", "14:10")], "days": {"Sun"}},
        "12605": {"name": "Express E", "stops": [("Coimbatore", "06:00", "06:10"), ("Salem", "08:00", "08:05"), ("Chennai", "12:00", "12:10")], "days": {"Mon", "Fri"}},
    }

def build_index(timetable):
    index = {}
    for train_no, info in timetable.items():
        for station, arrival, departure in info["stops"]:
            index.setdefault(station, []).append((train_no, arrival, departure, info["days"]))
    return index

def query_scan(timetable, station, day):
    found = []
    for train_no, info in timetable.items():
        if day in info["days"]:
            for stop, arrival, departure in info["stops"]:
                if stop == station:
                    found.append((train_no, info["name"], arrival, departure))
    return found

def query_index(index, timetable, station, day):
    return [(train_no, timetable[train_no]["name"], arr, dep)
            for train_no, arr, dep, days in index.get(station, []) if day in days]

def main():
    timetable = sample_timetable()
    for train_no, info in timetable.items():
        print(train_no, info["name"], info["stops"], sorted(info["days"]))
    print("Scan query:", query_scan(timetable, "Chennai", "Mon"))
    index = build_index(timetable)
    print("Indexed query:", query_index(index, timetable, "Chennai", "Mon"))
    print("Unknown station:", query_index(index, timetable, "Unknown", "Mon"))
    print("Departure at third stop of train 12601:", timetable["12601"]["stops"][2][2])

    rows = []
    for n in (100, 1_000, 10_000):
        big = {}
        for i in range(n):
            stops = [(f"Station{j}", "08:00", "08:05") for j in range(10)]
            big[str(i)] = {"name": f"Train{i}", "stops": stops, "days": {"Mon", "Wed"}}
        start = time.perf_counter(); idx = build_index(big); build_time = time.perf_counter()-start
        start = time.perf_counter()
        for _ in range(100):
            query_scan(big, "Station5", "Mon")
        scan_time = time.perf_counter()-start
        start = time.perf_counter()
        for _ in range(100):
            query_index(idx, big, "Station5", "Mon")
        index_time = time.perf_counter()-start
        memory = sys.getsizeof(idx)
        print(f"{n} trains: build_index={build_time:.6f}s scan100={scan_time:.6f}s index100={index_time:.6f}s index_shallow_bytes={memory}")
        rows.append([n, build_time, scan_time, index_time, memory])
    with open("q6_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["trains", "index_build_seconds", "scan_100_queries_seconds", "indexed_100_queries_seconds", "index_shallow_bytes"]); w.writerows(rows)

if __name__ == "__main__":
    main()
