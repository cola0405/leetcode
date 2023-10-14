class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row = column = 0
        for move in moves:
            if move == 'U':
                row -= 1
            elif move == 'D':
                row += 1
            elif move == 'L':
                column -= 1
            elif move == 'R':
                column += 1
        if row == 0 and column == 0:
            return True
        return False