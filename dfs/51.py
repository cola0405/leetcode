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


        def dfs(count):
            if count == n:
                ans.append([''.join(board[i]) for i in range(n)])
                return

            for j in range(n):  # 这个for循环即可做到当前row选其他column -- 精妙的"不选"
                if valid(count, j):
                    board[count][j] = 'Q'
                    dfs(count+1)  # 不用担心漏的问题，前面肯定dfs搜过
                    board[count][j] = '.'

        ans = []
        board = [['.']*n for _ in range(n)]
        dfs(0)
        return ans

res = Solution().solveNQueens(9)
for matrix in res:
    for row in matrix:
        print(row)
    print()
