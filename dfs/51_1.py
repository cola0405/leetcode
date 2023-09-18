# 极限压缩的优化方案
# 将皇后棋子的放置方案压缩到一个一维数组中！

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row, column):  # 检查当前点(row, column)是否有效
            for i in range(row):
                if board[i] == column:
                    return False
                # 当前点的横纵坐标如果与已放棋子的横纵坐标差值相等，则会在斜方向 -- 回忆斜线平移的图，可在leetcode官方题解找
                if abs(board[i] - column) == abs(i - row):  # 两边都取绝对值 -- 对应四个不同的斜线方向
                    return False
            return True

        def dfs(count):  # dfs搜索行，for循环搜索列
            if count == n:  # 下面的构造方法可以学习
                ans.append(['.'*board[i] + 'Q' + '.'*(n-board[i]-1) for i in range(n)])
                return

            for column in range(n):
                if valid(count, column):
                    board[count] = column  # 这个循环进入到if，则是当前row选其他column的情况 -- 精妙的"不选"
                    dfs(count+1)

        ans = []
        board = [0]*n  # 将皇后棋子的放置方案压缩到一个一维数组中！
        dfs(0)
        return ans

ret = Solution().solveNQueens(4)
for matrix in ret:
    for r in matrix:
        print(r)
    print()
