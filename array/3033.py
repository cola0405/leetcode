from typing import List
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [row[::] for row in matrix]
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == -1:
                    max_num = -1
                    for k in range(m):
                        max_num = max(max_num, mat[k][j])
                    mat[i][j] = max_num
        return mat
