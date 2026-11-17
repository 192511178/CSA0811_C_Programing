"""Task A4: logging, assertions, timing and profiling demonstration."""
import logging, time, cProfile

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

def clean_demo(values):
    result = []
    for value in values:
        if value is None:
            logging.warning("Missing reading skipped")
            continue
        assert isinstance(value, (int, float)), "Reading must be numeric"
        if value >= 0: result.append(value)
    return result

def workload():
    return sum(x*x for x in range(100_000))

if __name__ == "__main__":
    start = time.perf_counter()
    print("Cleaned:", clean_demo([48, None, -2, 95]))
    workload()
    print("Elapsed seconds:", time.perf_counter()-start)
    cProfile.run("workload()", sort="cumulative")
