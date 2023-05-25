from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)  # dp[i]表示金额达到i所需最小数量硬币
        dp[0] = 0
        # 无限背包问题，所以内层放coins
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

print(Solution().coinChange(coins = [1, 2, 5], amount = 11))

