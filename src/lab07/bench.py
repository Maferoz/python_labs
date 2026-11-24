import csv
from pathlib import Path
import random
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

SAMPLES_DIR = Path("data/samples/lab07")


def get_data(n):
    path = SAMPLES_DIR / f"numbers_{n}.csv"
    nums = []

    if path.exists() and path.stat().st_size > 0:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames and "value" in reader.fieldnames:
                for row in reader:
                    val = (row.get("value") or "").strip()
                    if val:
                        nums.append(int(val))

    if len(nums) != n:
        nums = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        path.parent.mkdir(parents=True, exist_ok=True)
        write_csv([["value"]] + [[str(x)] for x in nums], str(path))

    return nums[:n]


def bench_sorts(n, data):
    rows = []

    t_sorted = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", f"{t_sorted:.6f}"))

    sorts = [
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]

    for name, fn in sorts:
        if n >= 100_000:
            rows.append(("sort", n, name, "> 60 с"))
        else:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, f"{t:.6f}"))

    return rows


def bench_searches(data, queries_count=10_000):
    n = len(data)
    targets = [random.choice(data) for _ in range(queries_count // 2)] + [
        10**9 for _ in range(queries_count // 2)
    ]
    random.shuffle(targets)

    t_linear = timeit.timeit(
        lambda: [linear_search(data, x) for x in targets],
        number=1,
    )

    t_sort_for_bin = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)
    t_binary = timeit.timeit(
        lambda: [binary_search(sorted_data, x) for x in targets],
        number=1,
    )

    return [
        ("search", n, "linear_search", f"{t_linear:.6f}"),
        ("search", n, "sort_for_binary", f"{t_sort_for_bin:.6f}"),
        ("search", n, "binary_search", f"{t_binary:.6f}"),
    ]


def bench_two_sum(n, data):
    target = data[0] + data[-1]

    t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)

    return [
        ("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"),
        ("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"),
    ]


def print_table(rows):
    print(f"{'kind':<10} {'n':>8} {'algorithm':<18} {'time_sec':>12}")
    print("-" * 52)
    for kind, n, alg, t in rows:
        print(f"{kind:<10} {n:>8} {alg:<18} {t:>12}")


def main():
    random.seed(42)

    data_1k = get_data(1_000)
    data_10k = get_data(10_000)
    data_100k = get_data(100_000)

    all_rows = []

    for n, data in ((1_000, data_1k), (10_000, data_10k), (100_000, data_100k)):
        all_rows.extend(bench_sorts(n, data))

    all_rows.extend(bench_searches(data_100k, queries_count=10_000))

    for n, data in ((1_000, data_1k), (10_000, data_10k)):
        all_rows.extend(bench_two_sum(n, data))

    print_table(all_rows)

    csv_rows = [["kind", "n", "algorithm", "time_sec"]]
    for kind, n, alg, t in all_rows:
        csv_rows.append([kind, str(n), alg, str(t)])

    write_csv(csv_rows, "data/lab07/bench.csv")


if __name__ == "__main__":
    main()
#python3 -m src.lab07.bench