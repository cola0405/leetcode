# j往左是dp好的，直接累积就行
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        n = len(coins)

        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]

print(Solution().change(amount = 5, coins = [1, 2, 5]))