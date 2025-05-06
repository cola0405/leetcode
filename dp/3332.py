'''
dp + 图

题目大意：给了第 i天待在某城市的收益，以及从城市 a到城市 b的收益
允许从任意城市开始，问到第 k天，最大收益是多少

思路：
问题的关键点在于每天待在某一城市的收益会变化，所以没办法找单日最大收益，然后每天都执行
考虑 dp
dp[i] 肯定不足以表示状态，我们可能还需要明确当前状态是在哪一个城市
总而有 dp[i][j]表示第 i天在城市 j的最大收益
那状态怎么转移呢？
1.待在城市 j
2.从其他城市到 j
因为 n值小，所以直接枚举就完事了

'''


from typing import List
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0]*n for _ in range(k+1)]
        for i in range(k):              # 处理第 i天
            for j in range(n):          # 逐步处理各个城市 j
                dp[i+1][j] = dp[i][j] + stayScore[i][j]
                for p in range(n):      # 枚举各个城市到城市 j的情况
                    if p == j: continue
                    dp[i+1][j] = max(dp[i+1][j], dp[i][p] + travelScore[p][j])
        return max(dp[k])

print(Solution().maxScore(n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]))