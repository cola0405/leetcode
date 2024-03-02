# median greedy

from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_cost = sorted(zip(nums, cost))
        mid = (sum(cost)+1)//2
        cnt = 0
        for num, c in num_cost:
            cnt += c
            if cnt >= mid:
                ans = 0
                for x,c in num_cost:
                    ans += abs(x-num)*c
                return ans