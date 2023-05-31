from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = []
        visit = [0]*len(nums)
        def dfs(lst):
            if len(lst) == len(nums):
                # turn index to number
                p.append(lst[:])
                return
            for i in range(len(nums)):
                if visit[i] != 1:
                    # dfs
                    lst.append(nums[i])
                    visit[i] = 1
                    dfs(lst)

                    # 回溯
                    lst.pop()
                    visit[i] = 0
        dfs([])
        return p

print(Solution().permute(nums = [1,2,3]))

