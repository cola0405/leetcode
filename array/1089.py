from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nums = arr[:]
        i = j = 0
        n = len(arr)
        while i < len(arr):
            if nums[j] == 0:
                arr[i] = 0
                if i+1 < n:
                    arr[i+1] = 0
                i += 1
            else:
                arr[i] = nums[j]
            i += 1
            j += 1

print(Solution().duplicateZeros([1,0,2,3,0,4,5,0]))
