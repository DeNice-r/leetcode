def reverseWords(s):
    return ' '.join(map(lambda x: x[::-1], s.split()))


s = 'abc def mdmqkw mqwkldamsc s scmawq qpwo1293 smqdl'
print(reverseWords(s))
