from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def win(ch):
            row = [1]*3
            column = [1]*3
            diagonal = [1]*2
            for i in range(3):
                for j in range(3):
                    if board[j][i] != ch:
                        column[i] = 0
                    if board[i][j] != ch:
                        row[i] = 0
                if board[i][i] != ch:
                    diagonal[0] = 0
                if board[i][2-i] != ch:
                    diagonal[1] = 0
            return row.count(1) or column.count(1) or diagonal.count(1)

        player = 1
        board = [[0]*3 for _ in range(3)]
        res = {1: "A", -1: "B"}
        for x,y in moves:
            board[x][y] = player
            if win(player):
                return res[player]
            player *= -1
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

print(Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))

