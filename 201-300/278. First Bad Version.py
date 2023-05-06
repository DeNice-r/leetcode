import math as m


bad = -1


def isBadVersion(x):
    return x >= bad


def firstBadVersion(num_len) -> int:
    ctn = 0
    x = m.floor(num_len / 2)
    half = m.ceil(x / 2)
    mx = m.sqrt(num_len / 2)
    while ctn <= mx and x <= num_len:
        if isBadVersion(x):
            if x == 1:
                return 1
            if not isBadVersion(x - 1):
                return x
            x = x - half
        else:
            x = x + half
        half = m.ceil(half / 2)
        ctn += 1
    if isBadVersion(x):
        if not isBadVersion(x - 1):
            return x
    elif x < num_len and isBadVersion(x + 1):
        return x + 1


def test(n, lbad):
    global bad
    bad = lbad
    r = firstBadVersion(n)
    print(r)


test(5, 4)
