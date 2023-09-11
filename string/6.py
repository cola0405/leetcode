class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        matrix = [['']*n for _ in range(numRows)]
        row = 0
        column = 0
        step = 1
        i = 0
        while i<n:
            if row == numRows:
                row = max(0, numRows-2)
                column += 1
                for _ in range(numRows-2):
                    matrix[row][column] = s[i]
                    row -= 1
                    column += 1
                    i += 1
                    if i>=n:
                        break
            else:
                # vertical
                matrix[row][column] = s[i]
                row += 1
                i += 1
                if row == 0:
                    step *= -1

        ans = ''
        for i in range(numRows):
            for j in range(column+1):
                ans += matrix[i][j]
        return ans


print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))


