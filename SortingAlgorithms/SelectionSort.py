arr = [6,4,8,9,1,3,6,66,12,54,6,33,48,54,56,2,7,9,4,66]

def selection_sort1(arr:list) ->list:
    n = len(arr)
    for j in range(n - 1):
        minIndex = j
        for i in range(j + 1, n):
            if arr[i] < arr[minIndex]:
                minIndex = i
        minValue = arr.pop(minIndex)
        arr.insert(j, minValue)


def selection_sort2(arr:list) ->list:
    n = len(arr)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if arr[min_index] > arr[i]:
                min_index = i
        temp = arr[min_index]
        arr[min_index] = arr[j]
        arr[j] = temp
        #arr[min_index], arr[j] = arr[j], arr[min_index]
