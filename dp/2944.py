'''
题目有歧义
[26,18,6,12,49,7,45,45]
Purchase the 1st fruit with prices[0] = 26 coin, you are allowed to take the 2nd fruit for free.
Take the 2nd fruit for free.
Purchase the 3rd fruit for prices[2] = 6 coin, you are allowed to take the 4th, 5th and 6th (the next three) fruits for free.

根据测试用例可知，prices[i] 购入，则可以免费获得后续的 (i+1) 个水果
那么对于 dp[i] 就可以往前以 j枚举，找到能够覆盖到当前 i位的更少的花费

'''

from typing import List
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [float('inf') for _ in range(n+1)]     # dp[i] 表示获得前 i个水果，最少需要多少个金币
        # 初始状态
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] + prices[i-1]
            for j in range(i-1):
                if j + (j+1) >= i-1:
                    dp[i] = min(dp[i], dp[j] + prices[j])
        return dp[n]

print(Solution().minimumCoins([27,17,29,45,3,39,42,26]))