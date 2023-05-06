from math import ceil


def sortedSquares(nums):
    ptr = len(nums) - 1
    x, y = 0, ptr
    result = [0] * (ptr + 1)
    while x - y != 1:
        if abs(nums[x]) > nums[y]:
            result[ptr] = nums[x] ** 2
            x += 1
        else:
            result[ptr] = nums[y] ** 2
            y -= 1
        ptr -= 1
    return result


print(sortedSquares([-7, -3, 2, 3, 11]))
print(sortedSquares([-7]))
