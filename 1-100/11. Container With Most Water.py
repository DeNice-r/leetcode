from typing import List


def solve(height: List[int]) -> int:
    x, y, mx = [0] * 3

    while x < len(height) - 1:
        while y < len(height):
            mx = max(mx, (y - x) * min(height[x], height[y]))
            y += 1
        x += 1
        y = x + 1
    return mx


assert solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solve([1, 1]) == 1
