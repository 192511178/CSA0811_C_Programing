"""Q2: Tuples, mutability, aliasing, shallow/deep copy and grid construction."""
import copy, sys, time

def main():
    rows, cols = 3, 4
    bad = [[0] * cols] * rows
    bad[0][1] = 7
    good = [[0 for _ in range(cols)] for _ in range(rows)]
    good[0][1] = 7
    print("bad :", bad)
    print("good:", good)
    print(bad[0] is bad[1], good[0] is good[1])

    stops = {(13.0827, 80.2707): "Chennai Central",
             (13.0418, 80.2341): "T. Nagar"}
    print(stops[(13.0418, 80.2341)])
    try:
        stops[[13.0418, 80.2341]] = "Invalid key"
    except TypeError as exc:
        print("List key error:", exc)

    original = [[1, 2], [3, 4]]
    alias = original
    shallow = copy.copy(original)
    sliced = original[:]
    deep = copy.deepcopy(original)
    original[0][0] = 99
    print("alias sees change:", alias)
    print("shallow nested change:", shallow)
    print("deep copy independent:", deep)
    print("identity:", id(original), id(alias), id(shallow), id(deep))

    coordinates = [(13.08, 80.27), (13.04, 80.23)]
    for lat, lon in coordinates:
        print("Stop coordinate:", lat, lon)

    values = list(range(1_000_000))
    tuple_values = tuple(values)
    print("List size bytes:", sys.getsizeof(values))
    print("Tuple size bytes:", sys.getsizeof(tuple_values))
    for label, obj in (("list", values), ("tuple", tuple_values)):
        start = time.perf_counter()
        _ = obj[500_000]
        print(label, "index time:", time.perf_counter() - start)

    mixed = (1, [2, 3])
    mixed[1].append(4)
    print("Tuple containing mutable list:", mixed)

if __name__ == "__main__":
    main()
