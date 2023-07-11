
def solve(nums):
    # Neetcode solution, 'cause I thought that conversion to set and search in set are worse than O(n) and couldn't
    # figure out the solution.
    nset = set(nums)
    ln = 0

    for x in nset:
        l = 1
        if x - 1 not in nset:
            while x + l in nset:
                l += 1
        ln = max(ln, l)

    return ln


assert solve([100, 4, 200, 1, 3, 2]) == 4
assert solve([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
