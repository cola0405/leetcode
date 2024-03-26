# dfs + complex condition
from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        d = [(0,1),(0,-1),(1,-1),(1,0),(1,1),(-1,-1),(-1,0),(-1,1)]
        def dfs(i, j):
            if already[i][j]:
                return
            already[i][j] = 1
            board[i][j] = 'B'

            # check mine adjacent or not before dfs
            mine_adjacent = False
            next = []
            for k in range(8):
                d1,d2 = d[k]
                next_i,next_j = i+d1,j+d2
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                    continue
                if board[next_i][next_j] == 'M':
                    mine_adjacent = True
                next.append((i+d1, j+d2))

            for next_i,next_j in next:
                # stop spread when meet with "number" or "blank"
                if '1' <= board[next_i][next_j] <= '9' or board[next_i][next_j] == 'B':
                    continue
                if board[next_i][next_j] == 'M':
                    if '1' <= board[i][j] <= '9':
                        board[i][j] = str(int(board[i][j])+1)
                    else:
                        board[i][j] = '1'
                elif not mine_adjacent:
                    dfs(next_i,next_j)

        m = len(board)
        n = len(board[0])
        already = [[0]*n for _ in range(m)]
        cx,cy = click   # problem says the click would only be "M" or "E"
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
        else:
            dfs(click[0], click[1])
        return board

print(Solution().updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))