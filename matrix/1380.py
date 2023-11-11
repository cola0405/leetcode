from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        for i in range(m):
            min_idx = 0
            for j in range(1, n):
                if matrix[i][j] < matrix[i][min_idx]:
                    min_idx = j

            for j in range(m):
                if matrix[j][min_idx] > matrix[i][min_idx]:
                    break
            else:
                ans.append(matrix[i][min_idx])
        return ans

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))