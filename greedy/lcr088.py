from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ans = 0
        i = 0
        if cost[0] >= cost[1]:
            i += 1
        while i < n:
            ans += cost[i]
            if i+2 < n and cost[i+1] >= cost[i+2]:
                i += 2
            else:
                i += 1
            ans += cost[i]
        return ans
