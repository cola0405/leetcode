# dfs 的问题:
# [0,0,0]
# [#,f,f]
# [#,2,2]
# 对于(2,0)而言，不能往上，也就到这了它的最小距离为3



from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def dfs(row, column, d):
            if (row<0 or row>=m) or (column<0 or column>=n) or mat[row][column] == '#':
                return float('inf')

            if mat[row][column] == 0:
                return d
            if ans[row][column] != float('inf'):
                return ans[row][column]+d

            num = mat[row][column]
            mat[row][column] = '#'
            res = min(dfs(row+1, column, d+1),
                      dfs(row-1, column, d+1),
                      dfs(row, column+1, d+1),
                      dfs(row, column-1, d+1))
            mat[row][column] = num
            ans[row][column] = res - d
            return res

        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = dfs(i, j, 0)
        return ans

print(Solution().updateMatrix([[0,0,0],[1,1,1],[1,1,1]]))


