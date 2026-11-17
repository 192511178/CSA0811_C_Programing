"""Q6: Staircase recursion, memoisation, call counts and iterative alternative."""
import sys
from functools import lru_cache

naive_calls = 0
memo_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_iterative(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

def main():
    print("n=1..6 verification")
    for n in range(1, 7):
        print(n, ways_iterative(n))

    print("\nFunction-call measurements")
    for n in (10, 20, 25, 30):
        global naive_calls, memo_calls
        naive_calls = 0
        memo_calls = 0
        naive_result = ways_naive(n)
        naive_count = naive_calls
        ways_memo.cache_clear()
        memo_calls = 0
        memo_result = ways_memo(n)
        print(f"n={n}: naive result={naive_result}, calls={naive_count}; "
              f"memo result={memo_result}, calls={memo_calls}")

    print("\nPython recursion limit:", sys.getrecursionlimit())
    try:
        ways_memo.cache_clear()
        print("ways_memo(1000):", ways_memo(1000))
    except RecursionError as error:
        print("RecursionError at ways_memo(1000):", error)
    print("Iterative n=1000 has no recursive-depth issue; result digit count:",
          len(str(ways_iterative(1000))))

if __name__ == "__main__":
    main()
