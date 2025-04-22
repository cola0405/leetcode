'''
dp + 二分

这道题与 1751类似，额外的工作是需要同时保存收益最大的具体选择方案
那就在 dp数组中额外开空间，同时保存方案


'''

from typing import List
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        n = len(intervals)
        a = [(start, end, value, i) for i, (start, end, value) in enumerate(intervals)]
        a.sort(key=lambda x: x[1])
        dp = [[[0, []] for j in range(5)] for i in range(n+1)]
        for i in range(n):
            p = bisect.bisect_right(a, a[i][0]-1, hi=i, key=lambda x: x[1])
            for j in range(1, 5):       # 因为后面的状态会从 dp[p][j-1][1]转移而来，所以即使 j>i，我们也更新一下 dp
                # 不选当前区间 i
                dp[i+1][j][0] = dp[i][j][0]
                dp[i+1][j][1] = dp[i][j][1]

                # 选择当前区间 i
                val = dp[p][j-1][0] + a[i][2]
                if val > dp[i+1][j][0]:
                    dp[i+1][j][0] = val
                    dp[i+1][j][1] = sorted(dp[p][j-1][1] + [a[i][3]])
                elif val == dp[i+1][j][0]:
                    dp[i+1][j][1] = min(dp[i+1][j][1], sorted(dp[p][j-1][1] + [a[i][3]]))
        return dp[-1][4][1]

print(Solution().maximumWeight([[7,9,37],[20,24,36],[10,11,28],[23,25,19],[4,21,31],[1,3,9],[11,18,27],[25,25,40]]))