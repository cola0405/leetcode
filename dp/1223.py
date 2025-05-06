'''
多维 dp

题目大意：
摇 n次骰子，然后给了限制，每种数字不得连续超过 rollMax[num]次
问总共有多少种合法的数字序列

思路：
dp[i]表示前 i位的情况，还需要哪些信息位呢，某个数字已经连续多少次
那么就是 dp[i][j][k]表示在前 i位中，以数字 j结尾，且数字 j在末尾连续 k次的方案数
状态之间如何转移呢？
枚举前一个数字 p，如果数字 p与 j不同，则累加
如果 p==j，那么我们则需要从 [k-1]转移到 [k] (2 <= k <= rollMax[num])
如果 p!=j，那么以 p结尾的所有方案数都可以转移到 dp[i][j][1] 表示以 j结尾的连续 1次的方案数（因为当前数与前一个数不同）
'''

from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0]*16 for j in range(7)] for i in range(n+1)]
        for i in range(1,7):
            dp[1][i][1] = 1
        for i in range(1, n):
            for j in range(1, 7):
                for p in range(1, 7):       # 枚举前一个摇出的数
                    if j != p:
                        dp[i+1][j][1] += sum(dp[i][p])
                        dp[i+1][j][1] %= MOD
                    else:
                        for k in range(2, rollMax[j-1]+1):
                            dp[i+1][j][k] += dp[i][p][k-1]
                            dp[i+1][j][k] %= MOD

        ans = 0
        for j in range(1, 7):
            ans += sum(dp[n][j])
            ans %= MOD
        return ans

print(Solution().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
