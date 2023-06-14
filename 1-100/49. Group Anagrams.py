from time import time


def groupAnagrams(strs):
    r = []
    signatures = []
    for str in strs:
        s = {}

        for c in str:
            s[c] = s.setdefault(c, 0) + 1

        if s in signatures:
            r[signatures.index(s)].append(str)
        else:
            signatures.append(s)
            r.append([str])

    return r


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
