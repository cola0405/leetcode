class Solution:
    def solveEquation(self, equation: str) -> str:
        from collections import deque
        def f(s):
            res = 0
            num = '0'
            for ch in s:
                if ch not in "+-":
                    num += ch
                else:
                    q.append(ch)
                    op = q.popleft()
                    if op == '+':
                        res += int(num)
                    elif op == '-':
                        res -= int(num)
                    num = '0'
            print(res)
            return res

        left, right = equation.split('=')
        q = deque()
        for i in range(-4,-3):
            print(i)
            if f(left.replace('x', str(i))) == f(right.replace('x', str(i))):
                return "x="+str(i)

print(Solution().solveEquation("x+5-3+x=6+x-2"))




