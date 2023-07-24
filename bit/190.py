# 如何用异或给指定数位置1，学着点

# 另外还有一份实现：
"""
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n&1:
                res += 1
            res <<= 1
            n>>=1
        return res>>1
"""
# 末尾+1也是可以的，就是循环结束后别忘了把多余的左移操作给消掉



class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | n & 1
            n>>=1
        return res

print(Solution().reverseBits(2147483648))
