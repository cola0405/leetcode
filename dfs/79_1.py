# 字母不能重复使用 -- 还有矩阵标记+回溯。。

# dfs+回溯能过，但是7s 待优化
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(cur, i, j):
            if cur not in word:
                return False
            if cur == word:
                return True

            # 上下左右
            if i-1>=0 and available[i-1][j]:
                available[i-1][j] = 0
                res = dfs(cur+board[i-1][j], i-1, j)
                available[i-1][j] = 1
                if res:
                    return True
            if i+1<m and available[i+1][j]:
                available[i+1][j] = 0
                res = dfs(cur+board[i+1][j], i+1, j)
                available[i+1][j] = 1
                if res:
                    return True
            if j-1>=0 and available[i][j-1]:
                available[i][j-1] = 0
                res = dfs(cur+board[i][j-1], i, j-1)
                available[i][j-1] = 1
                if res:
                    return True
            if j+1<n and available[i][j+1]:
                available[i][j+1] = 0
                res = dfs(cur+board[i][j+1], i, j+1)
                available[i][j+1] = 1
                if res:
                    return True

            return False

        from collections import defaultdict
        m = len(board)
        n = len(board[0])
        available = [[1] * n for _ in range(m)]
        for k in range(m):
            for p in range(n):
                available[k][p] = 0
                if dfs(board[k][p],k,p):  # 从每一个位置开始去dfs试
                    return True
                available[k][p] = 1

        return False

print(Solution().exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))