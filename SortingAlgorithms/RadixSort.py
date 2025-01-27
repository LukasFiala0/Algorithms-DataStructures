array = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]

def radix_sort1(array:list):
    highest_radix = len(str(max(array)))

    for k in range(highest_radix):
        radix_array = [[] for i in range(10)]
        radix = 10 ** k

        for num in array:
            radix_num = (num // radix) % 10
            radix_array[radix_num].append(num)

        array = []

        for lst in radix_array:
            array.extend(lst)
               
    return array

def radix_sort2(array:list):
    maxVal = max(array)
    radix = 1

    while maxVal // radix > 0:
        radix_array = [[] for i in range(10)]
        while len(array) > 0:
            num = array.pop()
            radix_num = (num // radix) % 10
            radix_array[radix_num].append(num)

        for lst in radix_array:
            while len(lst) > 0:
                num = lst.pop()
                array.append(num)

        radix *= 10
    return array



print(radix_sort1(array))

print(radix_sort2(array))