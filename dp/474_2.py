# 递归的剪枝优化
# 600 的数据范围，也是可以剪枝递归AC的

# 最大为m n

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j][k] 到第i个字符串，0,1个数分别是j,k 的最多子串数
        dp = [[[0]*(n+1) for j in range(m+1)] for i in range(len(strs)+1)]

        for i in range(1,len(strs)+1):
            zero = strs[i-1].count('0')
            one = strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]

                    if j-zero >= 0 and k-one >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-zero][k-one]+1)
        return dp[-1][m][n]

print(Solution().findMaxForm(strs = ["0","0","1","1"], m = 2, n = 2))