from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


print(containsDuplicate(containsDuplicate, [1, 2, 3, 1]))
print(containsDuplicate(containsDuplicate, [1, 2, 3, 4, 5]))
