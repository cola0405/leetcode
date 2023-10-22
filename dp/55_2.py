# 某一位可以到target
# 再递归看那一位是否可达

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def reachable(target):
            if target == 0:
                return True
            for j in range(target):
                if j+nums[j] >= target:
                    return reachable(j)
            return False

        return reachable(len(nums)-1)

print(Solution().canJump([2,3,1,1,4]))
