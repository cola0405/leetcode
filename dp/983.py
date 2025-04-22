'''
一维线性 dp

比较经典的边界问题的处理方法
在个问题里，每个不同票的期限之间不会影响，可以对比 2140.py
'''

from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        s = set(days)                   # 用于判断当天是否是出行日
        dp = [0]*(last_day+1)           # dp[i] 表示满足[0,i]所有出行需求的最小花费
        for i in range(1, last_day+1):
            if i not in s:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(i-7,0)] + costs[1], dp[max(i-30,0)] + costs[2])
        return dp[-1]

print(Solution().mincostTickets(days = [1,4,6,7,8,365], costs = [2,7,15]))