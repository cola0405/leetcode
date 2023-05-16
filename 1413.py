from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 1
        s = 0
        for num in nums:
            s += num
            if s <= 0:
                res = max(abs(s)+1, res)
        return res

print(Solution().minStartValue([-3,2,-3,4,2]))
