'''
dp + 二分

是 1751的简化版本（没有参加会议最多 k的限制）

'''

from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        import bisect
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0]*(n+1)
        for i in range(n):
            dp[i+1] = dp[i]
            start = jobs[i][0]
            p = bisect.bisect_right(jobs, start, hi=i, key=lambda x: x[1])
            dp[i+1] = max(dp[i+1], dp[p] + jobs[i][2])
        return dp[-1]