# dfs 的问题:
# [0,0,0]
# [#,f,f]
# [#,2,2]
# 对于(2,0)而言，不能往上，也就到这了它的最小距离为3



from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        def bfs(row, column):
            q = deque()  # 0表示距离
            q.append((row, column, 0))
            while q:
                row, column, d = q.popleft()
                q.append((row+1,column, d+1))
                q.append((row-1, column, d+1))
                q.append((row, column+1, d+1))
                q.append((row, column-1, d+1))

                if (row<0 or row>=m) or (column<0 or column>=n) or visit[row][column] == mark:
                    continue

                visit[row][column] = mark
                if mat[row][column] == 0:
                    return d


        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        visit = [[0]*n for _ in range(n)]
        mark = 2
        for i in range(m):
            for j in range(n):
                ans[i][j] = bfs(i, j)
                mark += 1
        return ans

print(Solution().updateMatrix([[0],[0],[0],[0],[0]]))


