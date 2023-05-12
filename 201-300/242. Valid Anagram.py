
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    s_dict, t_dict = {}, {}
    for x in range(len(s)):
        if s[x] in s_dict: s_dict[s[x]] += 1
        else: s_dict[s[x]] = 1
        if t[x] in t_dict: t_dict[t[x]] += 1
        else: t_dict[t[x]] = 1

    return s_dict == t_dict


print(isAnagram("anagram", "nagaram"))
print(isAnagram("abcdef", "fabcdg"))
