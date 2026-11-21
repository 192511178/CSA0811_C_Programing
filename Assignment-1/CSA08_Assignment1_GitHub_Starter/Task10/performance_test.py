from decimal import Decimal
from time import perf_counter

def benchmark(count):
    values = ["33.40"] * count
    start = perf_counter()
    float_total = sum(float(x) for x in values)
    float_seconds = perf_counter() - start

    start = perf_counter()
    decimal_total = sum((Decimal(x) for x in values), Decimal("0.00"))
    decimal_seconds = perf_counter() - start

    print(f"Payments: {count:,}")
    print(f"Float total:   {float_total:.12f} ({float_seconds:.6f} s)")
    print(f"Decimal total: {decimal_total:.2f} ({decimal_seconds:.6f} s)")
    print(f"Difference:    {Decimal(str(float_total)) - decimal_total}")
    print()

if __name__ == "__main__":
    for n in (300, 6000, 150000):
        benchmark(n)
