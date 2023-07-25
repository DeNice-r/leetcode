def solve(nums, target=0):
    nums.sort()
    answer = []
    for x, v in enumerate(nums[:-2]):
        if x > 0 and nums[x - 1] == v:
            continue
        y, z = x + 1, len(nums) - 1
        while y < z:
            s = v + nums[y] + nums[z]
            if s > target:
                z -= 1
            else:
                if s == target:
                    answer.append((v, nums[y], nums[z]))
                y += 1
    return answer


assert solve([-1, 0, 1, 2, -1, -4]) == [(-1, -1, 2), (-1, 0, 1)]
assert solve([0, 0, 0, 0]) == [(0, 0, 0)]
