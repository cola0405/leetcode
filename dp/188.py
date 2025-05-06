from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, float('-inf')] for j in range(k+1)] for i in range(n+1)]  # 这里持有股票的收益初始要设置为负无穷
        for i in range(n):
            dp[i+1][0][1] = max(dp[i][0][1], dp[i][0][0]-prices[i])  # 这里表示在第 i天不持有股票的情况下购入（收益可能会是负数）
            for j in range(1, k+1):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i][j-1][1]+prices[i])
                dp[i+1][j][1] = max(dp[i][j][1], dp[i+1][j][0]-prices[i])
        return dp[-1][k][0]  # 到最后一天，进行 k笔交易，而且当前所以持有股票已卖出的最大收益