def radixsort(input_list):
    maxval = max(input_list)
    max_exponent = len(str(maxval))
    sortlist = input_list[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        digits = [[] for i in range(10)]
        for element in sortlist:
            element_str = str(element)
            try:
                digit = int(element_str[index])
            except IndexError:
                digit = 0
            digits[digit].append(element)
        sortlist = []
        for number in digits:
            sortlist.extend(number)

    return sortlist


test = [8, 435, 765, 2344534, 764, 1, 4534, 98, 44]
print(radixsort(test))
