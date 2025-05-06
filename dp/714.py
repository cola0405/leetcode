'''
多维dp

题目大意：交易的时候多了一个手续费

思路：dp购入股票的时候考虑进去即可
然后初始化的细节做好

'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -float('inf')] for _ in range(n+1)]
        dp[0][1] = -prices[0]
        for i in range(n):
            dp[i+1][0] = max(dp[i][0], dp[i][1] + prices[i] - fee)
            dp[i+1][1] = max(dp[i][1], dp[i+1][0] - prices[i])
        return dp[-1][0]

print(Solution().maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))