# 水往高处流
# dfs前判断，可以不需要last
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i, j, visited):
            if visited[i][j]:
                return
            visited[i][j] = 1
            if pf[i][j] and af[i][j]:
                ans.append([i,j])
            for k in range(4):
                if 0 <= i+d[k][0] < m and 0 <= j+d[k][1] < n\
                        and heights[i+d[k][0]][j+d[k][1]] >= heights[i][j]:
                    dfs(i+d[k][0],j+d[k][1],visited)

        m = len(heights)
        n = len(heights[0])
        pf = [[0]*n for _ in range(m)]  # Pacific ocean
        af = [[0]*n for _ in range(m)]  # Atlantic oceans

        ans = []
        for a in range(m):  # dfs from left and right
            dfs(a,0,pf)
            dfs(a,n-1,af)
        for a in range(n):  # dfs from top and bottom
            dfs(0,a,pf)
            dfs(m-1,a,af)
        return ans

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))