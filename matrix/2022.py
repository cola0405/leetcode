from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = [[0]*n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = original[idx]
                idx += 1
        return res

print(Solution().construct2DArray(original = [1,2,3,4], m = 2, n = 2))