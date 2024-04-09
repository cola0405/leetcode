from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        cnt = [(mat[i].count(1), i) for i in range(n)]
        cnt.sort()
        return [cnt[i][1] for i in range(k)]

print(Solution().kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))