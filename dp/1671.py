# 把山状数组拆成两个最长上升子序列，然后求最长公共子序即可
from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(a):
            n = len(a)
            dp = [1] * n
            for i in range(1,n):
                for j in range(i):
                    if a[i] > a[j]:     # 需要严格递增
                        dp[i] = max(dp[i],dp[j]+1)
            return dp
        
        l2r = LIS(nums)
        r2l = LIS(nums[::-1])[::-1]
        max_seq = 0
        for i in range(len(nums)):      
            if l2r[i] > 1 and r2l[i] > 1:       # 头尾不能作为山顶,且需要保证左右有元素
                max_seq = max(max_seq, l2r[i]+r2l[i])       
        return len(nums) - (max_seq-1)      # 山顶被重复算了两次
        
print(Solution().minimumMountainRemovals([100,92,89,77,74,66,64,66,64]))