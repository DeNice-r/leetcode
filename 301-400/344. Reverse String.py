def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    x = 0
    while x < len(s) / 2:
        s[x], s[-(x + 1)] = s[-(x + 1)], s[x]

        x += 1


st = ['d', 'e', 'n', 'y', 's']
reverseString(st)
print(st)