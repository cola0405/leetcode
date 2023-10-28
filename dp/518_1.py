# 3944ms
# 这道题不是正正的完全背包问题
# 所以不需要三重循环处理
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        n = len(coins)

        for j in range(n):
            for i in range(1, amount+1)[::-1]:
                for k in range(1, i//coins[j]+1):  # 取若干个
                    dp[i] += dp[i-k*coins[j]]
        return dp[amount]

print(Solution().change(amount = 5, coins = [1, 2, 5]))