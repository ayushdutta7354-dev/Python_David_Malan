#Two Pointers:

arr = [0,7,9,45,34,27,14];

arr = sorted(arr);

print(arr);


class Target:
    def target_sum(self, numbers:list[int],target:int) -> bool:
        i = 0;#1 pointer at extreme left
        j = len(numbers) -1; # another pointer extrmee right

        while i<j:
            sum = numbers[i] + numbers[j]; #current sum
            if sum < target:
                i+=1; #as sum < target, i should move forward to increase sum
            elif sum > target:
                j-=1; #as sum > target, j should move backward to decrese sum
            else:
                print(f"Sum found: {numbers[i]}, {numbers[j]}, {sum}");
                i+=1;
                j-=1;
        return False;



num_1 = Target();

num_1.target_sum(arr,41);

a = [45,67,21,42,-2,5,3,0,23,45];

a = sorted(a);

num_1.target_sum(sorted([45,67,21,42,-2,5,3,0,23,45]), 90);