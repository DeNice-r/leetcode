import math as m


def binarySearch(nums, target):
    ctn = 0
    num_len = len(nums)
    x = m.floor(num_len / 2)
    half = m.ceil(x / 2)
    mx = m.ceil(m.log(num_len)) + 1
    while ctn <= mx and x < num_len:
        if target < nums[x]:
            x = x - half
        elif target > nums[x]:
            x = x + half
        else:
            return x
        half = m. ceil(half / 2)
        ctn += 1
    if x >= num_len:
        x = num_len - 1
    if 0 <= x < num_len:
        if target == nums[x]:
            return x
        elif x > 0 and target == nums[x - 1]:
            return x - 1
        elif x < num_len - 1 and target == nums[x + 1]:
            return x + 1


def twoSum(nums, target):
    x = 0
    while x < len(nums):
        t = target - nums[x]
        index = binarySearch(nums, t)

        if index is not None and index != x:
            if x < index:
                return [x + 1, index + 1]
            else:
                return [index + 1, x + 1]
        x += 1


bruh = [-1] * 29998 + [1,1]
print(twoSum(bruh, 2))
