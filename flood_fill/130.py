# 从四周往中间搜索，搜索过的位置标记一下
# 搜索完之后，没被标记的即是被包围的


from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def mark_available(row, column):
            if (row<0 or row>=m) or (column<0 or column>=n)\
                or board[row][column] == 'X' or board[row][column] == 'A':
                return

            board[row][column] = 'A'
            mark_available(row+1, column)
            mark_available(row-1, column)
            mark_available(row, column+1)
            mark_available(row, column-1)

        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                mark_available(i, 0)
            if board[i][n-1] == 'O':
                mark_available(i, n-1)

        for i in range(n):
            if board[0][i] == 'O':
                mark_available(0, i)
            if board[m-1][i] == 'O':
                mark_available(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':    # 搜索过后仍然为'O'的则是被包围搜不到的
                    board[i][j] = 'X'
