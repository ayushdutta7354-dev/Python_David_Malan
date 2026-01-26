# Kadane's algo:

"""
Docstring for kadaneAlgorithm_7

given a arr, find the max sum in a given subarr.
"""


def subarr(arr: list[int]) -> int:
    curr_sum = 0
    ans = arr[0]

    for i in arr:
        curr_sum += i
        if curr_sum > ans:
            ans = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return ans


print(subarr([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
