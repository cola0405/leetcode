from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        # init
        for i in range(n):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                ans = 1
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                ans = 1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    ans = max(dp[i][j], ans)

        return ans**2

print(Solution().maximalSquare([["0","1"],["1","0"]]))
