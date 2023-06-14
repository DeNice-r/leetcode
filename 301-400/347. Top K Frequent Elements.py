def topKFrequent(nums, k):
    r = {}

    for n in nums:
        r[n] = r.setdefault(n, 0) + 1

    return sorted(r.keys(), key=lambda x: r[x], reverse=True)[:k]


# Solution, using built-ins (actually a little slower)
# def topKFrequent(nums, k):
#     r = Counter(nums)
#     return [*map(lambda x: x[0], r.most_common(k))]



print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
