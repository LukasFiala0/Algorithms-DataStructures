array = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]

def binary_search(array:list, value: int) ->int:
    array.sort()
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        elif value < array[middle]:
            right = middle - 1
        elif value > array[middle]:
            left = middle + 1
    return -1

def binary_search2(array:list, value: int, left:int, right:int) ->int:
    middle = (left + right) // 2
    if left > right:
        return -1
    if array[middle] == value:
        return middle
    elif value < array[middle]:
        right = middle - 1
        return binary_search2(array, value, left, right)
    elif value > array[middle]:
        left = middle + 1
        return binary_search2(array, value, left, right)

 
array.sort()
print(binary_search2(array, 66, 0, len(array) - 1))