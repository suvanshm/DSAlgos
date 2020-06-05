def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]


mylist = [8, 3, 5, 7, 1, 6, 9, 2]
bubble_sort(mylist)
print(mylist)
