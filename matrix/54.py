from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        u,d = 0, m-1
        l,r = 0, n-1
        while True:
            # 从左往右
            for i in range(l,r+1):
                ans.append(matrix[u][i])
            u += 1
            if u > d: return ans

            # 从上往下
            for i in range(u,d+1):
                ans.append(matrix[i][r])
            r -= 1
            if r < l: return ans

            # 从右往左
            for i in range(l,r+1)[::-1]:
                ans.append(matrix[d][i])
            d -= 1
            if d < u: return ans

            # 从下往上
            for i in range(u,d+1)[::-1]:
                ans.append(matrix[i][l])
            l += 1
            if l > r: return ans


print(Solution().spiralOrder([[2,5,8],[4,0,-1]]))
