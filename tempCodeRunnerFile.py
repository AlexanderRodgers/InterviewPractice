    while(j < max): #O(n^2) time
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
