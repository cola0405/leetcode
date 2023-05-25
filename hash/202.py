class Solution:
    def isHappy(self, n: int) -> bool:
        def new_num(num):
            res = 0
            for digit in str(num):
                digit = int(digit)
                res += digit**2
            return res

        s = set()
        while True:
            if n == 1:
                return True
            s.add(n)
            n = new_num(n)
            if n in s:
                return False