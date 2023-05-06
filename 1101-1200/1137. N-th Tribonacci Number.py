dp = [0, 1, 1]

def trib(n):
    if n < len(dp):
        return dp[n]

    for x in range(len(dp), n + 1):
        dp.append(dp[x - 3] + dp[x - 2] + dp[x - 1])

    return dp[n]


trib(0)
trib(1)
trib(2)
trib(3)
trib(4)
print(trib(0) == 0)
print(trib(1) == 1)
print(trib(2) == 1)
print(trib(3) == 2)
print(trib(4) == 4)
print(trib(25) == 1389537)


