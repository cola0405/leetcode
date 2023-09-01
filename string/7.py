class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        ans = 0
        while x>0:
            ans += x%10
            ans *= 10
            x //= 10
        ans = ans//10*sign
        return ans if -2**31<=ans<=2**31-1 else 0

print(Solution().reverse(-120))
