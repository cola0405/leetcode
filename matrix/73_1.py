# 十字标记法

# 利用两个标志位解决首行、首列的判定问题

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        first_row_flag = True if 0 in matrix[0] else False
        first_column_flag = True if 0 in [matrix[i][0] for i in range(m)] else False

        # 检查0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 十字首标记 -- 往前标记不会影响之后的
                    matrix[0][j] = 0

        for column in range(1,n):  # 先不处理特殊的第0行(标记用)
            if matrix[0][column] == 0:
                for k in range(m):
                    matrix[k][column] = 0  # 先不处理特殊的第0列
        for row in range(1,m):
            if matrix[row][0] == 0:
                for k in range(n):
                    matrix[row][k] = 0

        if first_row_flag:
            for column in range(n):
                matrix[0][column] = 0
        if first_column_flag:
            for row in range(m):
                matrix[row][0] = 0

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))


