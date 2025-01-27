
def insertion_sort1(arr):
    n = len(arr)
    for j in range(1,n):
        current_value = arr.pop(j)
        insert_index = j
        for i in range(j-1, -1, -1):
            if arr[i] > current_value:
                insert_index = i
        arr.insert(insert_index, current_value)
    return arr

def insertion_sort2(arr):
    n = len(arr)
    for j in range(1,n):
        current_position = j
        current_value = arr[j]
        while current_position > 0 and arr[current_position - 1] > current_value:
            arr[current_position] = arr[current_position - 1]
            current_position -= 1

        arr[current_position] = current_value

arr1 = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]
insertion_sort1(arr1)
print(arr1)
arr2 = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]
insertion_sort2(arr2)
print(arr2)