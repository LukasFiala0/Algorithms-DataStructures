array = [6, 4, 8, 9, 1, 3, 6, 66, 12, 54, 6, 33, 48, 54, 56, 2, 7, 9, 4, 66]

def linear_search(arr: list, val:int) -> int:
    n = len(arr)
    for i in range(n):
        if arr[i] == val:
            return i
    return -1
        
print(linear_search(array, 66))