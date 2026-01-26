# sliding window:
"""
1.
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.
"""


def subarr_sum(arr: list[int], k: int) -> int:
    current_sum = 0
    n = len(arr)
    for i in range(k):
        current_sum += arr[i]

    ans = current_sum / k

    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i - k]
        ans = max(ans, current_sum / k)

    return [ans, current_sum]


arr = [1, 12, -5, -6, 50, 3]

print(subarr_sum(arr, 4))


# 2. longest substr w/o repeatign char


def substr(s: str) -> int:
    set1 = set({})
    n = len(s)
    if n == 1:
        return n

    i = 0
    j = 1
    ans = 0
    set1.add(s[0])
    ans = 1

    while j < n:
        while s[j] in set1:
            set1.discard(s[i])
            i += 1
        set1.add(s[j])
        j += 1
        ans = max(ans,(j-i))

    return ans

print(substr("abacdbcd"));
print(substr("abacdbcdaaaaa"));
print(substr("abacdbcdefghi"));
