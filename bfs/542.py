# 0 其实是超级源点
# 从各个0开始bfs广播

# 不适用dfs的原因:
# [0,0,0]
# [#,f,f]
# [#,2,2]
# 对于(2,0)而言，不能往上，也就到这了它的最小距离为3



from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        pair = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i,j))

        # bfs
        while q:
            row, column = q.popleft()
            for p1, p2 in pair:
                x = row+p1
                y = column+p2

                if (x<0 or x>=m) or (y<0 or y>=n):
                    continue

                if ans[row][column]+1<ans[x][y]:  # 剪枝+更新最短距离
                    ans[x][y] = ans[row][column]+1
                    q.append((x, y))
        return ans

print(Solution().updateMatrix([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]))


