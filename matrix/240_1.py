from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0])-1

        while True:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1
            if row>=len(matrix) or column<0:
                return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))