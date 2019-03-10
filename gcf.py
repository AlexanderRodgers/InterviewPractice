test1 = [12, 16, 24]
test2 = [9, 81, 45, 90]
test3 = [100, 25, 60, 180]

def gcf(nums): # O(n) time
    min = 0
    for i in range(1, len(nums)):
        if nums[min] > nums[i]:
            min = i
    start = nums[min]
    max = len(nums)
    j = 0
    done = False
    while(not done): #O(n^2) time
        while(j < max):
            if nums[j] / start == nums[j] // start:
                if j + 1 == max:
                    return start
                j += 1
            else:
                if start == 1:
                    return start
                # we have to reset if the factor isn't the same across the list
                j = 0
                start -= 1

# total efficiency is O(n + n^2) => O(n^2)

print(gcf(test1))
print(gcf(test2))
print(gcf(test3))