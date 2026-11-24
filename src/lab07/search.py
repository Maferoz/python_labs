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