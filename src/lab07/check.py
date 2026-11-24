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