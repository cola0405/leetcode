# dual-monotonic stack
# base on problem 84, but use dual-monotonic stack for every column
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = [[0]*n for _ in range(m)]    # record the contiguous '1'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        left[i][j] = 1
                    else:
                       left[i][j] = left[i][j-1] + 1

        ans = 0
        for j in range(n):      # dual-monotonic stack for every column
            up = [-1]*m
            ms = []
            for i in range(m):
                while ms and left[i][j] <= left[ms[-1]][j]:
                    ms.pop()
                if ms:
                    up[i] = ms[-1]
                ms.append(i)

            down = [m]*m
            ms = []
            for i in range(m)[::-1]:
                while ms and left[i][j] <= left[ms[-1]][j]:
                    ms.pop()
                if ms:
                    down[i] = ms[-1]
                ms.append(i)

            for i in range(m):
                ans = max(ans, left[i][j] * (down[i]-up[i]-1))
        return ans

print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))