# binary search + greedy
from typing import List
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def fit(number):
            remain = budget
            for j in range(n):      # greedy iterate all requirements
                need = composition[i][j] * number
                if stock[j] < need:
                    remain -= (need - stock[j]) * cost[j]
            return remain >= 0

        ans = 0
        for i in range(k):      # try all k machines
            # binary search + greedy to calculate the number of machines that the budget could purchase
            low = 0
            high = int(1e9)
            while low < high:
                mid = (low+high+1)//2
                if fit(mid):
                    low = mid
                else:
                    high = mid-1

            ans = max(ans, low)
        return ans

print(Solution().maxNumberOfAlloys(n = 2, k = 5, budget = 48, composition = [[6,3],[9,5],[1,9],[1,8],[3,3]], stock = [4,8], cost = [10,1]))