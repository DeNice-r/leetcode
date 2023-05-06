from typing import List


def two_sum(nums: List[int], target: int) -> List[int] | None:
    remains = {}

    for x in range(len(nums)):
        if nums[x] in remains:
            return [remains[nums[x]], x]
        remain = target - nums[x]
        remains[remain] = x

    return None


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
