# 2d-array + game
from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotated = [[0]*m for u in range(n)]
        for i in range(n):
            for j in range(m):
                rotated[i][j] = box[-j-1][i]

        for u in range(m):  # deal with each column
            i = n-1
            j = n-1
            while j >= 0 and i >= 0:
                if rotated[j][u] != '.':
                    i -= 1
                    j -= 1
                    continue
                cnt = 0
                while i >= 0 and rotated[i][u] != '*':
                    if rotated[i][u] == '#':
                        rotated[i][u] = '.'
                        cnt += 1
                    i -= 1
                for k in range(cnt):
                    rotated[j][u] = '#'
                    j -= 1
                j = i
        return rotated

print(Solution().rotateTheBox([["#",".","*","."],["#","#","*","."]]))