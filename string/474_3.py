# 滚动数组优化

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j][k] 到第i个字符串，0,1个数分别是j,k 的最多子串数
        dp = [[[0]*(n+1) for j in range(m+1)] for i in range(2)]

        for i in range(1,len(strs)+1):
            zero = strs[i-1].count('0')
            one = strs[i-1].count('1')
            i = i%2
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zero][k-one]+1)
        return dp[i][m][n]

print(Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))