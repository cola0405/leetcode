# 降维优化+从右到左

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j][k] 到第i个字符串，0,1个数分别是j,k 的最多子串数
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(1,len(strs)+1):
            zero = strs[i-1].count('0')
            one = strs[i-1].count('1')
            for j in range(zero,m+1)[::-1]:
                for k in range(one, n+1)[::-1]:
                    dp[j][k] = max(dp[j][k], dp[j-zero][k-one]+1)
        return dp[m][n]

print(Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 50, n = 30))