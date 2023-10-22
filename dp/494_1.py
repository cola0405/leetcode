# dp[i][j] += dp[last][j-nums[i]] + dp[last][j+nums[i]]
# 前i个数，和为j的方法数
# 但是这样需要考虑负数的情况，得把列表开到2000
# 能过，但是会比较麻烦

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0]*2001 for _ in range(2)]
        # 前i个数，和为j的方法数
        dp[0][0] = 1
        last = 0
        cur = 1
        for i in range(n):
            for j in range(2001):
                dp[cur][j] = 0
                if j <= 1000:
                    # +nums[i]
                    if j-nums[i] >= 0:
                        dp[cur][j] += dp[last][j-nums[i]]
                    else:
                        dp[cur][j] += dp[last][(nums[i]-j)+1000]

                    # -nums[i] 超出范围的不处理 -- 能加出去的就能先减
                    if j+nums[i] <= 1000:
                        dp[cur][j] += dp[last][j+nums[i]]
                else:
                    # 大于1000后的-nums[i]已经和之前不一样了
                    # +
                    if j-1000 <= nums[i]:
                        dp[cur][j] += dp[last][nums[i] - (j-1000)]
                    else:
                        dp[cur][j] += dp[last][j-nums[i]]

                    if j+nums[i] <= 2000:
                        dp[cur][j] += dp[last][j+nums[i]]
            cur, last = last, cur

        if target >= 0:
            return dp[last][target]
        else:
            return dp[last][-target+1000]

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))