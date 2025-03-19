'''
列表中元素总和为s
则s一定为偶数，且一定存在一个子序列的和为s/2
dfs(i,target) 表示从[0,i] 是否存在和为target的子序列
则我们可以从dfs(n-1, s/2)开始搜索
对于每一个元素，我们可以选择选或者不选
'''

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, target):
            if i == 0:
                return target == 0 or target == nums[0] 
            return dfs(i-1, target) or dfs(i-1, target-nums[i])

        n = len(nums)
        s = sum(nums)
        return s%2 == 0 and dfs(n-1, s//2)

print(Solution().canPartition([1,5,11,5]))
        