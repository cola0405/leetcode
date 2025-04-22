'''
正向 dp会有问题
if j+questions[j-1][1] < i:     转移条件不能这么简单
可能存在这样一种情况
[i] 满足了 [j] 的条件
但是不满足更之前 [j-1]项的 brainpower 限制
如果再记录每个位置的 brainpower 这道题会变复杂，是否有不同的思路 详见2140.py
'''

from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = max(dp[i-1], questions[i-1][0])

            for j in range(1,i):
                if j+questions[j-1][1] < i:     # 转移条件不能这么简单
                    dp[i] = max(dp[i], dp[j]+questions[i-1][0])
        return dp[-1]

print(Solution().mostPoints([[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]))