class Solution:
    def solveEquation(self, equation: str) -> str:
        def f(e):
            e += '+'
            sign = 1
            c,x = 0,0
            seg = ''
            for ch in e:
                if ch not in '+-':
                    seg += ch
                else:
                    if 'x' in seg:
                        if len(seg) == 1:
                            x += sign
                        else:
                            x += sign * int(seg[:-1])
                    elif len(seg) > 0:
                        c += sign * int(seg)

                    seg = ''
                    sign = 1 if ch == '+' else -1

            return c,x

        left, right = equation.split('=')
        c1,x1 = f(left)
        c2,x2 = f(right)

        if c1 == c2 and x1 == x2:
            return "Infinite solutions"
        elif x1 == x2 or (c2-c1)%(x1-x2) != 0:
            return "No solution"
        else:
            return 'x=' + str((c2-c1)//(x1-x2))

print(Solution().solveEquation("-x=-1"))


