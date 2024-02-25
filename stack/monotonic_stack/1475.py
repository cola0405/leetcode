from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[::]
        s = []
        for i in range(len(prices)):
            while s and prices[i] <= prices[s[-1]]:
                inx = s.pop()
                ans[inx] = ans[inx] - prices[i]
            s.append(i)
        return ans

print(Solution().finalPrices([8,4,6,2,3]))