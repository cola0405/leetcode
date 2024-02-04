from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        ans = 0
        for i in range(1,len(pre)-1):
            if pre[i] >= pre[-1]-pre[i]:
                ans += 1
        return ans