from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = max(days)
        dp = [float('inf')]*(max_day+1)
        dp[0] = 0
        the_days = set(days)
        days.insert(0,0)
        for day in range(1,max_day+1):
            if day in the_days:
                prev = [day-1, max(day-7,0), max(day-30,0)]
                for j in range(3):
                    dp[day] = min(dp[prev[j]]+costs[j], dp[day])
            else:
                dp[day] = dp[day-1]
        return dp[max_day]

print(Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))