'''
多维 dp

题目大意：最多两次交易，问最大股票收益是多少

思路：
比较棘手的是我们不可能 i之前所有的卖出情况枚举出来
那应该怎么记录状态来进行 dp呢
考虑到最多 2笔交易，所以不难想到 dp[i][j] 表示第 i天进行了 j次交易的最大收益
但是还有一个问题，如果我在第 i天决定卖出，那我怎么知道第 i天手上恰好有股票呢？
所以，我们需要给 dp再加一层：dp[i][j][0/1] 分别表示第 i天不持有(0)/ 持有(1)股票的最大收益
那么此时状态如何转移呢？

dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + price[i])
dp[i-1][j][0] 表示第 i天不做任何操作
dp[i-1][j-1][1] + price[i] 表示我在 i-1天持有股票的情况下，在第 i天卖出    （这里 j-1是因为此处卖出后，第二笔股票交易完成，所以是从第一笔转移而来）

dp[i][j][1] = max(dp[i-1][j][1], dp[i][j][0] - price[i])
dp[i-1][j][1] 表示第 i天不做任何操作
dp[i-1][j][0] - price[i] 表示在第 i天没有股票的情况下购入股票

提高扩展，如果固定 k笔，请看题目 188 (把 2改为 k即可)
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, float('-inf')] for j in range(3)] for i in range(n+1)]       # 这里持有股票的收益初始要设置为负无穷
        for i in range(n):
            dp[i+1][0][1] = max(dp[i][0][1], dp[i][0][0]-prices[i])             # 这里表示在第 i天不持有股票的情况下购入（收益可能会是负数）
            for j in range(1,3):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i][j-1][1] + prices[i])
                dp[i+1][j][1] = max(dp[i][j][1], dp[i+1][j][0] - prices[i])
        return dp[-1][2][0]     # 到最后一天，进行 2笔交易，而且当前所以持有股票已卖出的最大收益


print(Solution().maxProfit([6,1,3,2,4,7]))