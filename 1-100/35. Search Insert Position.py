import math as m


def searchInsert(nums, target) -> int:
    ctn = 0
    num_len = len(nums)
    x = m.floor(num_len / 2)
    half = m.ceil(x / 2)
    mx = m.ceil(m.log(num_len))
    while ctn <= mx and x < num_len:
        if target < nums[x]:
            x = x - half
        elif target > nums[x]:
            x = x + half
        else:
            return x
        half = m.ceil(half / 2)
        ctn += 1
    if x >= num_len:
        return num_len
    if x <= 0:
        if target > nums[0]:
            return 1
        return 0
    if target < nums[x]:
        return x
    return x + 1


vals = [
    # [searchInsert([1, 3, 5, 6], 5), 2],
    # [searchInsert([1, 3, 5, 6], 2), 1],
    # [searchInsert([1, 3, 5, 6], 7), 4],
    # [searchInsert([1, 2, 4, 6, 7], 3), 2],
    # [searchInsert([3, 5, 7, 9, 10], 8), 3],
    # [searchInsert([1, 2, 4, 6, 8, 9, 10], 10), 6],
    # [searchInsert([1], 2), 1],
    [searchInsert([1, 3, 5], 2), 1],
]

print('\n'.join([f'{x[0]} == {x[1]} => {x[0] == x[1]}' for x in vals]))
