from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dfs(row, column, total):
            if row == len(matrix):
                return total
            if (column<0 or column == len(matrix)
                    or total+matrix[row][column]>record[row][column]):
                return float('inf')

            num = matrix[row][column]
            record[row][column] = min(total+num, record[row][column])
            return min(dfs(row+1, column-1, total+num),
                       dfs(row+1, column, total+num),
                       dfs(row+1, column+1, total+num))


        ans = float('inf')
        n = len(matrix)
        record = [[float('inf')]*n for _ in range(n)]
        for i in range(len(matrix)):
            ans = min(dfs(0, i, 0), ans)
        return ans

print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
