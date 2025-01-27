arr = [3,8,5,2,1]
n = len(arr)
minVal = arr[0]
for i in arr:
    if minVal > i:
        minVal = i
        
print(minVal)
