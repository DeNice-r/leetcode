from typing import List


# O(n + m) solution
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    len_sum = len(nums1) + len(nums2)
    median_index = len_sum // 2 + 1

    x, y, current, prev = [0] * 4

    while x < len(nums1) or y < len(nums2):
        if y == len(nums2) or (x != len(nums1) and nums1[x] < nums2[y]):
            current, prev = nums1[x], current
            x += 1
        else:
            current, prev = nums2[y], current
            y += 1
        if median_index == x + y:
            if len_sum % 2:
                return current
            else:
                return (prev + current) / 2


n1, n2 = [1, 3], [2]
print(find_median_sorted_arrays(n1, n2))
n1, n2 = [1, 2], [3, 4]
print(find_median_sorted_arrays(n1, n2))
