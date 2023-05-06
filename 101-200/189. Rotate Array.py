def rotate(nums, k):
    if k == 0 or len(nums) == k or len(nums) == 1:
        return
    rots = 0
    st_index = 0
    index = st_index
    temp = nums[0]
    div = len(nums) / k
    is_multi = div > 1
    while rots < len(nums):
        tidx = (index + k) % len(nums)
        nums[tidx], temp = temp, nums[tidx]
        index = tidx
        rots += 1
        if is_multi and round(rots % div, 10) == 0:
            st_index += 1
            index = st_index
            temp = nums[st_index]


nums = [1, 2, 3, 4, 5, 6, 7, 8]
rotate(nums, 2)
print(nums)
