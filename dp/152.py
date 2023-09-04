# 咸鱼翻身dp

# 同时存储dp_max和dp_min 就可以解决问题
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [-float('inf')]*(n+1)
        dp_min = [float('inf')]*(n+1)

        dp_max[1] = nums[0]
        dp_min[1] = nums[0]

        for i in range(1,n):
            dp_max[i+1] = max(nums[i], nums[i]*dp_max[i], nums[i]*dp_min[i])
            dp_min[i+1] = min(nums[i], nums[i]*dp_max[i], nums[i]*dp_min[i])
        return max(dp_max)

print(Solution().maxProduct([2,3,-2,4]))
