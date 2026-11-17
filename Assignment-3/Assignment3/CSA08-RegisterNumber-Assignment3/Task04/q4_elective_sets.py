"""Q4: Elective registration clash detection using sets."""
import random, time, csv

def reports(ai_elective, iot_elective, all_students):
    both = ai_elective & iot_elective
    exactly_one = ai_elective ^ iot_elective
    neither = all_students - (ai_elective | iot_elective)
    return sorted(both), sorted(exactly_one), sorted(neither)

def benchmark():
    rows = []
    for n in (10_000, 100_000, 1_000_000):
        data = list(range(n)); data_set = set(data); target = n - 1
        for name, container in (("list", data), ("set", data_set)):
            start = time.perf_counter()
            for _ in range(100):
                target in container
            elapsed = time.perf_counter() - start
            print(f"n={n} {name} 100 membership checks: {elapsed:.6f}s")
            rows.append([n, name, elapsed])
    with open("q4_membership_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["size", "container", "seconds_for_100_checks"]); w.writerows(rows)

def main():
    ai_elective = {"192311001", "192311004", "192311007", "192311009"}
    iot_elective = {"192311002", "192311004", "192311009", "192311010"}
    all_students = {f"1923110{i:02d}" for i in range(1, 11)}
    both, exactly_one, neither = reports(ai_elective, iot_elective, all_students)
    print("clash :", both)
    print("exactly one:", exactly_one)
    print("neither :", neither)
    # Equivalent set-method implementation
    print("Methods match:", both == sorted(ai_elective.intersection(iot_elective))
          and exactly_one == sorted(ai_elective.symmetric_difference(iot_elective))
          and neither == sorted(all_students.difference(ai_elective.union(iot_elective))))
    print("Empty electives:", reports(set(), set(), all_students))
    print("Identical electives:", reports(ai_elective, ai_elective, all_students))
    benchmark()

if __name__ == "__main__":
    main()
