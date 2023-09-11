class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        for num in range(10**n):
            num = str(num)
            if len(num) == len(set(num)):
               ans += 1
        return ans

print(Solution().countNumbersWithUniqueDigits(6))