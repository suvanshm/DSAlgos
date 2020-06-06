def selectionsort(arr):
    for i in range(len(arr)):
        minidx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[minidx], arr[i] = arr[i], arr[minidx]
    return arr


test = [8, 2, 6, 3, 4, 9, -3, 1]
print(selectionsort(test))
