# 传统计数
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        i = 0
        target = len(arr)*0.25
        while i<len(arr)-1:
            count = 1
            while i<len(arr)-1 and arr[i] == arr[i+1]:
                count += 1
                i += 1
            if count > target:
                return arr[i]
            i += 1

print(Solution().findSpecialInteger([1]))