# binary search the bound + maximum maintain
import bisect
from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        n = len(difficulty)
        items = sorted([(difficulty[i], profit[i]) for i in range(n)])
        difficulty = []
        profit = []
        for i in range(n):
            difficulty.append(items[i][0])
            profit.append(items[i][1])

        max_profit = 0      # maintain the maximum
        cur = 0
        ans = 0
        for k in worker:
            index = bisect.bisect_right(difficulty, k)  # upper bound
            for i in range(cur, index):
                max_profit = max(max_profit, profit[i])
            ans += max_profit
            cur = index
        return ans
