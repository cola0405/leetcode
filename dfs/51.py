from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row, column):  # row column 用于平移 画图可知个方向的表达式
            for i in range(n):
                if board[i][column] == 'Q' or board[row][i] == 'Q'\
                    or (0<=row-i<n and 0<=column-i<n and board[row-i][column-i] == 'Q')\
                    or (row+i<n and column+i<n and board[row+i][column+i] == 'Q') \
                    or (row+i<n and 0<=column-i<n and board[row+i][column-i]=='Q') \
                    or (0<=row-i<n and column+i<n and board[row-i][column+i]=='Q'):
                        return False  # 上下移动即可
            return True

        def dfs(row):
            if row == n:
                ans.append([''.join(line) for line in board])
                return

            for column in range(n):
                if valid(row, column):
                    board[row][column] = 'Q'
                    dfs(row+1)
                    board[row][column] = '.'

        ans = []
        board = [['.']*n for _ in range(n)]
        dfs(0)
        return ans