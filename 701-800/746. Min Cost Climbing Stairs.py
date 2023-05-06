from typing import List


# def min_cost_climbing(cost: List[int]) -> int:
#     n = len(cost)
#     dp = [0] * (n + 1)
#
#     for x in range(2, n + 1):
#         dp[x] = min(dp[x - 1] + cost[x - 1], dp[x - 2] + cost[x - 2])
#
#     return dp[n]


# Space-optimized solution
def min_cost_climbing(cost: List[int]) -> int:
    n = len(cost)
    current, prev1, prev2 = [0]*3

    for x in range(2, n + 1):
        current = min(prev1 + cost[x - 1], prev2 + cost[x - 2])
        prev1, prev2 = current, prev1

    return current


v = min_cost_climbing([10, 15, 20])
print(v, v == 15)
v = min_cost_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(v, v == 6)
v = min_cost_climbing([0, 0, 0, 1])
print(v, v == 0)
v = min_cost_climbing([0, 1, 1, 1])
print(v, v == 1)
v = min_cost_climbing([1, 0, 0, 2])
print(v, v == 0)
