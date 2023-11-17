# 使用for循环+递归实现：拿/不拿

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, i):
            ans.append(cur)
            for x in range(i,len(nums)):
                dfs(cur+[nums[x]], x+1)

        ans = []
        dfs([], 0)
        return ans

print(Solution().subsets([1,2,3]))