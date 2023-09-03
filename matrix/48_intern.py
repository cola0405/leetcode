# 原地修改矩阵完成旋转

# 花瓣替换，只需要一圈一圈旋转即可

#   左     上
# (2,0)->(0,0)
# (1,0)->(0,1)
# (0,0)->(0,2)

# 补全后为：右->下->左->上
# 找相邻两边的规律即可 -- 从上往下扫一眼就知道了

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            # 外圈环转90°
            for j in range(i, n-i-1):  # debug看，3x3的只需要转两圈就够了
                tmp = matrix[i][j]  # 备份上
                matrix[i][j] = matrix[n-j-1][i]  # 左到上
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]  # 下到左
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]  # 右到下
                matrix[j][n-i-1] = tmp  # 上到右

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))

