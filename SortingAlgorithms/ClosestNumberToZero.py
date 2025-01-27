# https://leetcode.com/problems/find-closest-number-to-zero/description/

nums = [-4, -2, 1, 4, 8, 2]

def findClosestNumber(nums):
    distances = []
    for val in nums:
        distances.append(abs(val))
    return min(distances)
print(findClosestNumber(nums))

