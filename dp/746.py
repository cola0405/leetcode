from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        ans = [0]*n
        for i in range(2,n):
            ans[i] = min(ans[i-1]+cost[i-1], ans[i-2]+cost[i-2])
        return ans[-1]

print(Solution().minCostClimbingStairs([10,15,20]))