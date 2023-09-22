# 8皇后求棋子摆放方案数


def valid(row, column):  # 检查当前点(row, column)是否有效
    for i in range(row):
        if board[i]==column:
            return False
        # 两边都取绝对值 -- 对应四个不同的斜线方向
        if abs(board[i]-column)==abs(i-row):
            return False
    return True


def dfs(row):  # dfs搜索行，for循环搜索列
    if row == 8:
        return 1

    res = 0
    for column in range(8):
        if valid(row, column):
            board[row] = column
            res += dfs(row+1)
    return res

board = [0]*8  # 压缩棋盘
print(dfs(0))


