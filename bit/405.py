# 没法处理负数补码表示的情况

class Solution:
    def toHex(self, num: int) -> str:
        res = ''
        h = [str(i) for i in range(10)] + [chr(97+i) for i in range(6)]
        while num > 0:
            digit = num%16
            res = h[digit] + res
            num //= 16
        return res

print(Solution().toHex(26))