from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        return [[original[i*n+j] for j in range(n)] for i in range(m)]

print(Solution().construct2DArray(original = [1,2,3,4], m = 2, n = 2))