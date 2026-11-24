## A. Поиск (search.py)

```
def linear_search(nums, x):
    for i, val in enumerate(nums):
        if val == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Возвращает индекс элемента x в отсортированном списке sorted_nums или -1.

    На неотсортированном списке результат не определён.
    """
    if not sorted_nums or x < sorted_nums[0] or x > sorted_nums[-1]:
        return -1

    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = sorted_nums[mid]
        if mid_val == x:
            return mid
        if mid_val < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
```


## B. Сортировки (sorting.py)

```
def bubble_sort(x):
    arr = list(x)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(x):
    arr = list(x)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def selection_sort(x):
    arr = list(x)
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
## C. Проверка против эталона (check.py)
```
import random
from src.lab07.search import binary_search,linear_search,two_sum_brute,two_sum_fast
from src.lab07.sorting import bubble_sort,insertion_sort,selection_sort


def check_sorting(fn, trials=100):
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        result = fn(nums)

        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
        checks += 1
    return checks


def check_search(trials=100):
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 100)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        # Проверяем существующий элемент (первое вхождение) и отсутствующее число
        candidates = []
        if nums:
            candidates.append(random.choice(nums))
        candidates.append(10_000)

        for x in candidates:
            actual = linear_search(nums, x)
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1

            assert actual == expected, (
                f"linear_search({nums}, {x}) вернул {actual}, ожидалось {expected}"
            )
            assert nums == original, "linear_search изменила исходный список"
            checks += 1

        # Бинарный поиск работает только на отсортированном списке
        s_nums = sorted(nums)
        s_original = list(s_nums)

        test_targets = [10_000, -10_000]
        if s_nums:
            test_targets.extend([s_nums[0], s_nums[-1], random.choice(s_nums)])

        for x in test_targets:
            idx = binary_search(s_nums, x)
            assert s_nums == s_original, "binary_search изменила исходный список"

            if x in s_nums:
                assert idx != -1, f"binary_search не нашёл существующий {x} в {s_nums}"
                assert 0 <= idx < len(s_nums), f"binary_search вернул индекс вне границ: {idx}"
                assert s_nums[idx] == x, (
                    f"binary_search вернул индекс {idx} со значением {s_nums[idx]}, ожидалось {x}"
                )
            else:
                assert idx == -1, (
                    f"binary_search вернул {idx} для отсутствующего {x} в {s_nums}, ожидалось -1"
                )
            checks += 1

    return checks


def check_two_sum(trials=100):
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 60)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        # Иногда делаем target гарантированно существующим, иногда — случайным
        if len(nums) >= 2 and random.random() < 0.7:
            i, j = random.sample(range(len(nums)), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-200, 200)

        ans_brute = two_sum_brute(nums, target)
        ans_fast = two_sum_fast(nums, target)

        assert nums == original, "two_sum изменила исходный список"

        if ans_brute is None:
            assert ans_fast is None, (
                f"two_sum_brute вернул None, а two_sum_fast вернул {ans_fast} "
                f"для nums={nums}, target={target}"
            )
        else:
            i, j = ans_brute
            assert isinstance(i, int) and isinstance(j, int) and 0 <= i < j < len(nums), (
                f"two_sum_brute вернул некорректные индексы {ans_brute} для nums={nums}"
            )
            assert nums[i] + nums[j] == target, (
                f"two_sum_brute пара {ans_brute} не даёт target={target} в {nums}"
            )

            assert ans_fast is not None, (
                f"two_sum_brute нашёл {ans_brute}, а two_sum_fast вернул None "
                f"для nums={nums}, target={target}"
            )
            fi, fj = ans_fast
            assert isinstance(fi, int) and isinstance(fj, int) and 0 <= fi < fj < len(nums), (
                f"two_sum_fast вернул некорректные индексы {ans_fast} для nums={nums}"
            )
            assert nums[fi] + nums[fj] == target, (
                f"two_sum_fast пара {ans_fast} не даёт target={target} в {nums}"
            )

        checks += 1

    return checks


if __name__ == "__main__":
    random.seed(42)
    total_checks = 0

    for fn in (bubble_sort, insertion_sort, selection_sort):
        total_checks += check_sorting(fn)

    total_checks += check_search()
    total_checks += check_two_sum()

    print(f"OK: {total_checks} проверок")
```
## D. Бенчмарк (bench.py)
```
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
```
> INPUT: -m src.lab07.bench


> OUTPUT: <img width="373" height="297" alt="Screenshot 2026-11-24 at 23 03 58" src="https://github.com/user-attachments/assets/8877903c-560e-4bf4-91cb-122ce87f3227" />
