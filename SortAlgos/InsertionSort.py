def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


test = [8, 3, 5, 7, 1, 6, 9, 2]
insertionsort(test)
print(test)
