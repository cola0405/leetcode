# 73_1 有十字标记法

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zero_pos = []  # 记录位置
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_pos.append((i,j))  # 不能直接修改，会影响后续判断

        for row,column in zero_pos:
            # deal with current row
            for k in range(n):
                matrix[row][k] = 0

            # deal with current column
            for k in range(m):
                matrix[k][column] = 0



