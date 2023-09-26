from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high = len(matrix[i])-1
            while low < high:
                mid = (low+high)//2
                if matrix[i][mid] >= target:
                    high = mid
                else:
                    low = mid+1
            if matrix[i][low] == target:
                return True
        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))