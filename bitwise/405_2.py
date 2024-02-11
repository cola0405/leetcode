class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        res = ''
        count = 0
        while num != 0 and count < 8:
            digit = num&0xf
            res = (str(digit) if digit < 10 else chr(97+digit-10)) + res
            num >>= 4
            count += 1
        return res

print(Solution().toHex(26))