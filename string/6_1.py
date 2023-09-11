# 抽象的数据结构

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['']*numRows
        step = -1
        i = 0

        for ch in s:
            res[i] += ch
            if i == numRows-1 or i == 0:
                step *= -1
            if numRows > 1:
                i += step

        return ''.join(res)




print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))


