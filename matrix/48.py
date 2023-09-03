# 利用额外的列表帮助旋转
# 自己列转化找规律
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n-i-1] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]

