arr = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]

def counting_sort_1(arr:list):
    count = [0] * (max(arr) + 1)
    i = 0
    while i <= len(arr) - 1:
        count[arr[i]] += 1
        i += 1
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr


def counting_sort_2(arr:list):
    count = [0] * (max(arr) + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

def counting_sort_3(arr:list):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return arr

print(counting_sort_1(arr))
print(counting_sort_2(arr))
print(counting_sort_3(arr))