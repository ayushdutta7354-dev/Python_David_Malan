"""
Docstring for 3_ProblemSolvingTechnique.pivot_index_4

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index’s right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

def pivot_index(arr: list) -> int:
    left_sum = 0
    total_sum = sum(arr)

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    
    return -1;


print(pivot_index([3,4,1,7]));
print(pivot_index([3,4,1,7, 8]));