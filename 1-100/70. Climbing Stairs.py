dp = [0, 1, 2]


def climbing(n: int) -> int:
    if n < len(dp):
        return dp[n]

    for x in range(len(dp), n + 1):
        dp.append(dp[x - 1] + dp[x - 2])

    return dp[n]


print(climbing(0))
print(climbing(1))
print(climbing(2))
print(climbing(3))
print(climbing(4))
print(climbing(30))
