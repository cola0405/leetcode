# 通过擦脚印+回溯的方法解决复用问题

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, target):
            if target == len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n \
                    or board[i][j] != word[target]:
                return False

            letter = board[i][j]
            board[i][j] = ''
            # 上下左右
            if dfs(i-1, j, target+1) or dfs(i+1, j, target+1)\
                or dfs(i, j-1, target+1) or dfs(i, j+1, target+1):
                return True
            board[i][j] = letter
            return False

        m = len(board)
        n = len(board[0])
        for k in range(m):
            for p in range(n):
                if dfs(k,p,0):  # 从每一个位置开始去dfs试
                    return True
        return False

print(Solution().exist(board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))