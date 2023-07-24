import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a<=b:
            s = a**2 + b**2
            if s == c:
                return True
            elif s > c:
                b -= 1
            else:
                a += 1
        return False

print(Solution().judgeSquareSum(3))
