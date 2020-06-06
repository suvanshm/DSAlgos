# Recursive
def binarysearch(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarysearch(arr, target, start, mid - 1)
    else:
        return binarysearch(arr, target, mid + 1, end)


# test = [3, 7, 11, 14, 21, 46]
# result = binarysearch(test, 49, 0, len(test)-1)
# print(result)


# Iterative

def binarysearch2(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] < target:
            low = mid + 1
    return -1


test = [3, 7, 11, 14, 21, 46]
result = binarysearch2(test, 46)
print(result)
