"""Q3: Farmer helpline complaint word frequency, district grouping and benchmarks."""
import random, re, time, csv
from collections import Counter

CALLS = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def tokenise(text):
    return re.findall(r"[a-z]+", text.lower())

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in tokenise(text):
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def frequencies_setdefault(texts, stop):
    counts = {}
    for text in texts:
        for word in tokenise(text):
            if word not in stop:
                counts.setdefault(word, 0)
                counts[word] += 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

def group_by_district(records):
    grouped = {}
    for district, crop, complaint in records:
        grouped.setdefault(district, []).append({"crop": crop, "complaint": complaint})
    return grouped

def benchmark():
    rows = []
    vocabulary = ["seed", "water", "price", "pest", "fertiliser", "subsidy", "crop"]
    for n in (1_000, 10_000, 100_000):
        texts = [" ".join(random.choices(vocabulary, k=8)) for _ in range(n)]
        methods = [
            ("dictionary", lambda: frequencies(texts, set())),
            ("list_count", lambda: [all_words.count(w) for w in distinct]),
            ("Counter", lambda: Counter(all_words)),
        ]
        all_words = [w for text in texts for w in tokenise(text)]
        distinct = set(all_words)
        for name, func in methods:
            start = time.perf_counter(); func(); elapsed = time.perf_counter() - start
            print(f"{n} complaints | {name}: {elapsed:.6f}s")
            rows.append([n, name, elapsed])
    with open("q3_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["complaints", "method", "seconds"]); w.writerows(rows)

def main():
    counts = frequencies(CALLS, STOP)
    print(top(counts, 3))
    records = [
        ("Thanjavur", "rice", "seed not received"),
        ("Salem", "mango", "pest attack"),
        ("Thanjavur", "rice", "irrigation issue"),
    ]
    print("District grouping:", group_by_district(records))
    print("setdefault result:", frequencies_setdefault(CALLS, STOP))
    benchmark()

if __name__ == "__main__":
    main()
