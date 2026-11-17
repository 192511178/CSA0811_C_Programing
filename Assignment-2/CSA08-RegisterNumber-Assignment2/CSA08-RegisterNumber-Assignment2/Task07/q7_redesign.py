"""Q7: Diagnose naive recursion and validate memoised/iterative redesign."""
import time
import csv
from functools import lru_cache

naive_calls = 0
memo_calls = 0

def original_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return original_naive(n - 1) + original_naive(n - 2)

@lru_cache(maxsize=None)
def redesigned_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return redesigned_memo(n - 1) + redesigned_memo(n - 2)

def redesigned_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def timed(function, n):
    start = time.perf_counter()
    result = function(n)
    return result, time.perf_counter() - start

def main():
    rows = []
    for n in (10, 20, 25, 30):
        global naive_calls, memo_calls
        naive_calls = 0
        original_result, original_time = timed(original_naive, n)
        original_count = naive_calls

        redesigned_memo.cache_clear()
        memo_calls = 0
        memo_result, memo_time = timed(redesigned_memo, n)
        memo_count = memo_calls

        iterative_result, iterative_time = timed(redesigned_iterative, n)
        assert original_result == memo_result == iterative_result
        print(f"n={n}: result={original_result}")
        print(f"  naive: calls={original_count}, time={original_time:.6f}s")
        print(f"  memo:  calls={memo_count}, time={memo_time:.6f}s")
        print(f"  loop:  time={iterative_time:.6f}s")
        rows.append([n, original_result, original_count, original_time,
                     memo_count, memo_time, iterative_time])

    with open("comparison_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "result", "naive_calls", "naive_seconds",
                         "memo_calls", "memo_seconds", "iterative_seconds"])
        writer.writerows(rows)
    print("All three methods returned matching results.")
    print("Saved comparison_results.csv in the current working directory.")

if __name__ == "__main__":
    main()
