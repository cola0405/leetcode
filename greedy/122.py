from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans

print(Solution().maxProfit([7,6,4,3,1]))

