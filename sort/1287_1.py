# 这个思路太好玩了
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        gap = int(len(arr)*0.25)
        for i in range(len(arr)):
            j = i+gap
            if i+gap < len(arr) and arr[i] == arr[j]:
                return arr[i]

print(Solution().findSpecialInteger([1]))