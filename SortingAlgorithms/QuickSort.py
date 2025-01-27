arr = [10, 16, 8, 12, 15, 6, 3, 9, 5, 20]
def partition1(l,h, arr):
    pivot = arr[l]
    i = l + 1
    j = h
    while i <= j:
        lower = None
        higher = None
        if arr[i] > pivot:
            higher = arr[i]

        if arr[j] <= pivot:
            lower = arr[j]

        if lower and higher:
            arr[i], arr[j] = lower, higher
            i += 1
            j -= 1

        if not higher:
            i += 1
        
        if not lower:
            j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort(arr, l, h):
    if l < h:
        p = partition1(l, h, arr)
        quick_sort(arr, l, p)
        quick_sort(arr, p + 1, h)

# Better implementation of partition
def partition2(l, h, arr):
    pivot = arr[l]
    i = l + 1
    j = h
    while i <= j:
        while i <= h and arr[i] <= pivot:
            i += 1

        while j >= l and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

quick_sort(arr, 0, len(arr)-1)
print(arr)