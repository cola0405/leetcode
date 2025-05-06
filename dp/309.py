'''
多维 dp

题目大意：额外设置了一天的冷冻期无法进行股票交易，求最大收益

思路：
dp[i][0/1] 表示在第 i天未持有或持有股票的最大收益（[0]相当于就表示有股票也给卖出去了）
下面要就状态转移
首先 dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
不买入股票时，转移是照常就行
但是买入股票就不能从 i-1转移而来了，而应该是 i-2
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - price[i])

然后额外要注意的就是初始状态的设置，第一天购入股票收益为负，这个我们得手动设置一下
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,float('-inf')] for _ in range(n+1)]         # 持有股票的最大收益应该初始化为负无穷
        dp[1][1] = -prices[0]       # 表示在第一天购入股票，收益暂时会是负的，这个初始状态我们得设置好
        for i in range(1, n):       # i==0的情况上面已经初始化好了，这里直接从 1开始，也为了避免下面[i-1]越界的问题
            dp[i+1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i+1][1] = max(dp[i][1], dp[i-1][0] - prices[i])
        return dp[-1][0]

print(Solution().maxProfit([1]))
