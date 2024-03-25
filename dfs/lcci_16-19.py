from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or already[i][j] or land[i][j] != 0:
                return 0
            already[i][j] = 1
            return (dfs(i-1,j) + dfs(i+1, j) + dfs(i,j-1) +
                    dfs(i,j+1) + dfs(i-1,j-1) + dfs(i-1,j+1) +
                    dfs(i+1,j-1) + dfs(i+1,j+1)) + 1

        m = len(land)
        n = len(land[0])
        already = [[0]*n for _ in range(m)]
        ans = []
        for a in range(m):
            for b in range(n):
                if land[a][b] == 0:
                    res = dfs(a,b)
                    if res > 0:
                        ans.append(res)
        ans.sort()
        return ans

print(Solution().pondSizes([
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]))