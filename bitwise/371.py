class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        bit = 1
        carry = 0
        while a > 0 or b > 0:
            res |= (a&bit) ^ (b&bit)
            if 
            bit <<= 1

