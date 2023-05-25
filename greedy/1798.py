from typing import List
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 1
        for i in range(len(coins)):  # 题目要求必须从0开始的连续整数
            if ans >= coins[i]:  # (0,n)可达，且(n+1)>=coin 那么(0,n+coin)便可达
                ans += coins[i]
        return ans

print(Solution().getMaximumConsecutive(coins = [1,1,1,4]))