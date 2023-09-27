# 9x9 到 3x3

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0]*10 for _ in range(10)]
        column = [[0]*10 for _ in range(10)]
        cells = [[[0]*10 for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])

                row[i][num] += 1        # 一趟能定一行
                column[j][num] += 1     # 双重循环走完了才能确定所有列，但可以在标记时就看是否>1
                cells[i//3][j//3][num] += 1  # 处理3x3

                if row[i][num] > 1 or column[j][num] > 1 \
                        or cells[i//3][j//3][num] > 1:
                    return False
        return True

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))