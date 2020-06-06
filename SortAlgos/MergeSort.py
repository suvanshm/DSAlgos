def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_sort = merge_sort(lst[:middle])
    right_sort = merge_sort(lst[middle:])

    return merge(left_sort, right_sort)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


# Testing
test = [8, 3, 5, 7, 1, 6, 9, 2]
print(test)
print(merge_sort(test))
