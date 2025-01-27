def bubble(arr:list) -> list:
    for j in range(len(arr)):
        sorted = True
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                swap = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = swap
        if sorted == True:
            break
arr = [6,4,8,9,1,3,6,66,12,54,6,33,48,54,56,2,7,9,4,66]
print(arr)