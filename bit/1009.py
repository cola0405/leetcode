class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        copy = n
        mask = 0
        while copy > 0:
            mask <<= 1
            mask |= 1
            copy >>= 1

        return n ^ mask

print(Solution().bitwiseComplement(5))