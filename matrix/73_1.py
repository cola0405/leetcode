from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        start = 1 if matrix[0][0]!=0 else 0

        # 检查0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 十字首标记 -- 往前标记不会影响之后的
                    matrix[0][j] = 0

        for column in range(1,n)[::-1]:
            if matrix[0][column] == 0:
                for k in range(m):
                    matrix[k][column] = 0
        for row in range(m)[::-1]:
            if matrix[row][0] == 0:
                for k in range(n):
                    matrix[row][k] = 0
            if start == 0:
                matrix[row][0] = 0

        print()


print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


