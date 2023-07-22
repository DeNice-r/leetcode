from typing import List


def search(collection: List, item):
    low, high = 0, len(collection) - 1

    while low <= high:
        index = (low + high) // 2
        if collection[index] < item:
            low = index + 1
        elif collection[index] > item:
            high = index - 1
        else:
            return index

    return None


def solve(nums, target):
    x = 0
    while x < len(nums):
        t = target - nums[x]
        index = search(nums, t)

        if index is not None and index != x:
            return [min(x + 1, index + 1), max(x + 1, index + 1)]
        x += 1


assert solve([-1] * 29998 + [1, 1], 2) == [29999, 30000]
assert solve([2, 3, 4], 6) == [1, 3]
assert solve([-1, -1] + [1] * 5, -2) == [1, 2]
