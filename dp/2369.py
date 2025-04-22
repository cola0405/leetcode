'''
划分型 dp、一维线性 dp

'''

from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n+1)        # dp[i] 表示 nums[0:i] 是否可以满足要求
        dp[0] = True
        for i in range(1, n+1):
            j = i-1                 # offset
            if i-1 >= 0 and dp[i-2] and nums[j] == nums[j-1]:
                dp[i] = True
            if i-3 >= 0 and dp[i-3] \
                    and (nums[j] == nums[j-1] == nums[j-2] or nums[j] == nums[j-1]+1 == nums[j-2]+2):
                dp[i] = True
        return dp[-1]

print(Solution().validPartition([4,4,4,5,6]))
