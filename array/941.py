from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        while i<len(arr)-1 and arr[i] < arr[i+1]:
            i += 1

        j = len(arr)-1
        while j>0 and arr[j]<arr[j-1]:
            j -= 1

        if 0<i<len(arr)-1 and i == j:
            return True
        return False

print(Solution().validMountainArray(arr = [0,3,2,1]))
