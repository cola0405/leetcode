# dfs标识出不同岛 + bfs找最短路

# 为什么不用dfs找最短路？
# dfs 会花多余的时间在不是最短路的路径上！！！（同时还没办法略过bfs的小步数）
# 而bfs找最短路更合适 -- 一步一步往外找，一旦找到，就是最短路径



from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        n = len(grid)

        def mark_island(row, column):
            if ((row<0 or row>=n) or (column<0 or column>=n)
                    or grid[row][column] == flag):
                return
            if grid[row][column] == 0:
                q.append((row, column, 0))  # 环岛的出发点，放入队列
                return

            grid[row][column] = flag
            mark_island(row+1, column)
            mark_island(row-1, column)
            mark_island(row, column+1)
            mark_island(row, column-1)

        # 先划出两座岛的范围
        done = False
        flag = 2
        for i in range(n):
            if done: break
            for j in range(n):
                if grid[i][j] == 1:
                    mark_island(i, j)
                    done = True
                    break

        ans = float('inf')
        record = [[float('inf')]*n for _ in range(n)]
        pair = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            row, column, count = q.popleft()
            if count>=min(record[row][column], ans):
                continue

            record[row][column] = count
            if grid[row][column] == 1:
                return count

            for dx, dy in pair:
                x, y = row+dx, column+dy
                if (0 <= x < n) and (0 <= y < n) and grid[x][y]!=2:
                    q.append((x, y, count+1))

print(Solution().shortestBridge([[0,1],[1,0]]))


