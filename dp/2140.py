'''
线性 dp

正向 dp会有问题 详见2140.py
'''

from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)      # dp[i] 表示剩余[i,n-1]这些题目能获得的最大分数
        for i in range(n)[::-1]:
            j = min(i+questions[i][1]+1, n)
            dp[i] = max(dp[i+1], dp[j] + questions[i][0])
        return dp[0]

print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))