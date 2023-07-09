from typing import List


def solve(nums: List[int]) -> List[int]:
    nums_len = len(nums)
    answer = [1] * nums_len
    for i in range(1, nums_len):
        answer[i] = answer[i - 1] * nums[i - 1]

    rvalue = 1
    for i in range(nums_len - 1, -1, -1):
        answer[i] *= rvalue
        rvalue *= nums[i]
    return answer


assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solve([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
