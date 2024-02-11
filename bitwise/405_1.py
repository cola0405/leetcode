class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        res = ''
        h = [str(i) for i in range(10)] + [chr(97+i) for i in range(6)]
        count = 0
        while num != 0 and count < 8:
            res = h[num&0xf] + res
            num >>= 4
            count += 1
        return res

print(Solution().toHex(-1))