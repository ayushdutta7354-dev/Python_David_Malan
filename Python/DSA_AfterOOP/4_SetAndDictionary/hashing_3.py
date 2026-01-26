#Hashing

#1. two sum- arr unsorted

arr = [2,1,8,4,6,3,9,5];#unsorted arr

def two_sum(arr:list[int], target: int)->list:
    n = len(arr)
    d1 = {}

    for i in range(n):
        rem = target - arr[i]
        if rem in d1:
            return [d1[rem],i]
        d1[arr[i]] = i
        # print(d1);


print(two_sum(arr, 10))
print(two_sum(arr, 14))
print(two_sum(arr, 7))