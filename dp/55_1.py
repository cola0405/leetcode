# 贪心，一步一步往左边推 -- O(n)
# 能到i的肯定可以到i-1

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-1
        while i > 0:
            flag = 1
            for j in range(i)[::-1]:
                if j+nums[j] >= i:
                    i = j
                    flag = 0
                    break
            if flag:
                return False
        return True

print(Solution().canJump([2,3,1,1,4]))
