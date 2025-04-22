'''
区间 dp
（效率不如 dfs，原因是没有剪枝，硬怼 O(n^2)）

这里的重点是 —— 只存在三种操作分数
所以用不着去开到三维 dp

'''


from typing import List
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def solve(score):
            max = lambda a, b: b if b>a else a      # 手写 max 更快！
            n = len(nums)
            dp = [[0]*n for _ in range(n)]  # dp[i][j] 表示[i,j]操作分数数为 score 的最多操作数
            for i in range(n)[::-1]:
                for j in range(i+1, n):
                    if i+2 < n and nums[i] + nums[i+1] == score:
                        dp[i][j] = max(dp[i][j], dp[i+2][j] + 1)
                    if j-2 >= 0 and nums[j-1] + nums[j] == score:
                        dp[i][j] = max(dp[i][j], dp[i][j-2] + 1)
                    if i+1 < n and j-1 >= 0 and nums[i] + nums[j] == score:
                        dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 1)
            return dp[0][-1]

        res1 = solve(nums[0] + nums[1])
        res2 = solve(nums[-1] + nums[-2])
        res3 = solve(nums[0] + nums[-1])
        return max(res1, res2, res3)

print(Solution().maxOperations([1,1,1,1,1,1,2,1,1,2]))