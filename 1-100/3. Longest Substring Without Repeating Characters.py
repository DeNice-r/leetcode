


def lognestSubstr(s: str):
    if len(s) < 2:
        return len(s)
    mx = 1
    for x in range(len(s)):
        found = False
        if len(s) - x < mx:
            break
        for y in range(x + 1, len(s)):
            if s[y] in s[x:y]:
                length = y - x
                found = True
                if length > mx:
                    mx = length
                break
        if y == len(s) - 1:
            if not found and y - x + 1 > mx:
                mx = y - x + 1
            if x - y < mx:
                break
    return mx


print(lognestSubstr("abcabcbb"))
print(lognestSubstr("abcdef123"))
print(lognestSubstr("abcde abcdefg"))
print(lognestSubstr("abcdeabcdaqwertyuio"))
