def solve(nums, target):
    x, y = 0, len(nums) - 1
    s = nums[x] + nums[y]
    while s != target:
        if s > target:
            y -= 1
        else:
            x += 1
        s = nums[x] + nums[y]
    return x + 1, y + 1


assert solve([-1] * 29998 + [1, 1], 2) == (29999, 30000)
assert solve([2, 3, 4], 6) == (1, 3)
assert solve([-1, -1] + [1] * 5, -2) == (1, 2)
