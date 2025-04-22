'''
dp + 二分

题目大意：
在 n个会议中选择 k个会议，会议时间要求不重叠，求最大的收益

思路：
不能像 2054那样去另辟蹊径了，只能硬着 dp上
同样无法针对各个时刻去 dp（10^9）
这里的状态设置为 dp[i][j] 前 i个会议中选择 j个会议的最大收益（ 1235那题就不需要把 dp开到 2维）
dp[i][j] 从哪个状态转移而来呢？ —— 左边第一个不重叠的区间 p
这里可以通过排序(根据结束时间排序) + 二分来找
dp[i][j] = max(dp[i][j], dp[p][j-1] + value)
'''


from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        import bisect
        n = len(events)
        events.sort(key=lambda x: x[1])
        dp = [[0]*(k+1) for _ in range(n+1)]
        ans = 0
        for i in range(n):
            start = events[i][0]
            # 找到 i之前的第一个不重叠区间
            # start-1 是因为题目有要求，会议时间区间端点不能重叠
            p = bisect.bisect_right(events, start-1, hi=i, key=lambda e: e[1])
            for j in range(1, k+1):         # 因为后面的状态会从 dp[p][j-1]转移而来，所以即使 j>i，我们也更新一下 dp
                # dp[i+1] 是处理偏移问题
                dp[i+1][j] = dp[i][j]       # 不开当前会议
                dp[i+1][j] = max(dp[i+1][j], dp[p][j-1] + events[i][2])
                ans = max(ans, dp[i+1][j])
        return ans

print(Solution().maxValue([[1,2,4],[3,4,3],[2,3,1]], k = 2))