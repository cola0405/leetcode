from typing import List
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        width = n
        height = m
        for a,b in ops:
            height = min(height, a)
            width = min(width, b)
        return width*height


print(Solution().maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))