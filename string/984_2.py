class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def build(s, a1, b1):
            if a1 == 0 and b1 == 0:
                return s

            # 放a还是放b
            if a1 > 0 and (len(s) <= 1 or s[-2:] != 'aa'):
                res = build(s+'a', a1-1, b1)
                if len(res) == a+b:
                    return res
            if b1 > 0 and (len(s) <= 1 or s[-2:] != 'bb'):
                res = build(s+'b', a1, b1-1)
                if len(res) == a+b:
                    return res
            return ''

        return build('',a,b)


print(Solution().strWithout3a3b(a = 3, b = 5))



