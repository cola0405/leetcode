# 字母不能重复使用 -- 还有矩阵标记+回溯。。

# dfs+回溯能过，但是7s 待优化
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(pos, row, column):
            if (row<0 or row>=m) or (column<0 or column>=n)\
                    or board[row][column] != word[pos] or not available[row][column]:
                return False
            if pos == len(word)-1:
                return True

            available[row][column] = 0

            # 上下左右
            pos += 1  # 搜索下一个字母
            if dfs(pos, row-1, column)\
                or dfs(pos, row+1, column)\
                or dfs(pos, row, column-1)\
                or dfs(pos, row, column+1):
                return True

            available[row][column] = 1  # 回溯
            return False

        m = len(board)
        n = len(board[0])
        available = [[1] * n for _ in range(m)]

        # 优化 -- word前面重复多，后面重复少，可以从把word翻转再搜索
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    count += 1
                elif board[i][j] == word[-1]:
                    count += 1
        if count > 0:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):  # 从每一个位置开始去dfs试
                    return True
        return False

print(Solution().exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))