class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n%2 == 0:
                n //= 2
                ans += 1
            else:
                n -= 1
                n //= 2
                ans += 2
        return ans

print(Solution().integerReplacement(7))