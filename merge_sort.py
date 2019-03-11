unordered = [23, 65, 3, 54, -500, 43, 5032, 42, 46, 100]

def merge_sort(my_list):

    if len(my_list) > 1:

        middle = len(my_list) // 2

        # Make sure to slice the middle correctly.
        left = my_list[:middle]
        right = my_list[middle:]

        # Make sure to understand that lists are objects that are passed by reference.
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
    return my_list

print(merge_sort(unordered))