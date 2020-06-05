from random import randrange


# Implementing a simple approach


def qs(lst):
    if len(lst) <= 1:
        return lst
    less, more = [], []
    pivot = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            less.append(lst[i])
        else:
            more.append(lst[i])
    less_sorted = qs(less)
    more_sorted = qs(more)
    return less_sorted + [pivot] + more_sorted


# Testing
# test = [8, 4, 7, -9, 0, 2, 5]
# print(test)
# print(qs(test))


# Implementing an in-place approach


def quicksort(lst, start, end):
    if start >= end:
        return
    pivot_idx = randrange(start, end + 1)
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]
    less_pointer = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[less_pointer], lst[i] = lst[i], lst[less_pointer]
            less_pointer += 1
    lst[end], lst[less_pointer] = lst[less_pointer], lst[end]
    quicksort(lst, start, less_pointer - 1)
    quicksort(lst, less_pointer + 1, end)


# Testing
test2 = [6, 1, 4, 3, 9, 11, 0, -3]
print(test2)
quicksort(test2, 0, len(test2) - 1)
print(test2)
