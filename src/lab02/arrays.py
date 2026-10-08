def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''Возвращает кортеж из минимума и максимума для списка, состоящего из чисел'''
    if not nums:
        raise ValueError()
    mini = nums[0]
    maxi = nums[0]
    for i in nums:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    return mini, maxi

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает список из отсортированных по возрастанию уникальных чисел"""
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)
    for i in range(len(unique_nums)):
        for u in range(len(unique_nums)-i-1):
            if unique_nums[u] > unique_nums[u+1]:
                unique_nums[u], unique_nums[u+1] = unique_nums[u+1], unique_nums[u]
    return unique_nums

def flatten(mat: list[list | tuple]) -> list :
    '''Возвращает список из список/кортежей из списка'''
    res = []
    for i in nums:
        if type(i) != tuple and type(i) != list:
            raise TypeError()
        res.extend(i)
    return res

                       


    



