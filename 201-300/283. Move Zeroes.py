

def moveZeroes(nums):
    x = 0
    offset = 0
    while x < len(nums):
        if nums[x] != 0:
            nums[x - offset] = nums[x]
        else:
            offset += 1
        x += 1
    nums[len(nums) - offset:] = [0] * offset


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
