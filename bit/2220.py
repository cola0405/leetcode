class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        digits = start^goal
        count = 0
        while digits > 0:
            if digits&1:
                count += 1
            digits >>= 1
        return count

print(Solution().minBitFlips(10,7))