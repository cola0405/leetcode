from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        from collections import defaultdict
        def win(row, column, ch):  # 朝各个方向进行检查
            res = 1
            for i in range(1,3):
                if row+i < 3 and board[row+i][column] == ch:
                    res += 1
            if res == 3: return True

            res = 1
            for i in range(1, 3):
                if column+i<3 and board[row][column+i]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if row-i>=0 and board[row-i][column]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if column-i>=0 and board[row][column-i]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if row+i<3 and column+i<3 and board[row+i][column+i]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if row-i>=0 and column-i>=0 and board[row-i][column-i]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if row+i<3 and column-i>=0 and board[row+i][column-i]==ch:
                    res += 1
            if res==3: return True

            res = 1
            for i in range(1, 3):
                if row-i>=0 and column+i<3 and board[row-i][column+i]==ch:
                    res += 1
            if res==3: return True

            return False

        count = defaultdict(int)
        win_count = defaultdict(int)
        for i in range(3):
            for j in range(3):
                c = board[i][j]
                count[c] += 1
                if win(i, j, c):
                    win_count[c] += 1

        # 检查数量
        if count["O"] > count["X"] or count["X"] - count["O"] > 1:
            return False

        # 如果有winner则需要额外检查数量
        if win_count["X"] + win_count["O"] > 0:
            if ((win_count["X"]>win_count["O"] and count["X"]>count["O"])
                or (win_count["O"]>win_count["X"] and count["X"]==count["O"])):
                return True
            else:
                return False
        # 数量没问题、无winner 则为True
        return True

print(Solution().validTicTacToe(board = ["XOX","O O","XOX"]))