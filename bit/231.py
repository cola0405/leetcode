# 1000 & 0111 = 0
# 只有2的幂才会使得 n&(n-1) = 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n&(n-1) == 0

print(Solution().isPowerOfTwo(1))
