from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        num = 1
        u, d = 0, n-1
        l, r = 0, n-1
        while True:
            for i in range(l, r+1):
                matrix[u][i] = num
                num += 1
            u += 1
            if u>d: return matrix

            for i in range(u, d+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            if r<l: return matrix

            for i in range(l, r+1)[::-1]:
                matrix[d][i] = num
                num += 1
            d -= 1
            if d<u: return matrix

            for i in range(u, d+1)[::-1]:
                matrix[i][l] = num
                num += 1
            l += 1
            if l>r: return matrix

print(Solution().generateMatrix(3))