import re


def solve(s: str):
    pattern = r'[^a-z0-9]'
    s = re.sub(pattern, '', s.lower())

    i, j = 0, len(s) - 1
    while i < len(s) and j >= 0:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


assert solve('A man, a plan, a canal: Panama')
assert solve('race a car') is False
assert solve('0F') is False
