from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]
            if coins == 0:
                return i+1
            elif coins < 0:
                return i
        return len(costs)

print(Solution().maxIceCream(costs = [1,6,3,1,2,5], coins = 20))