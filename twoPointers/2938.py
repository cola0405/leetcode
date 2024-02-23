class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        j = n-1
        ans = 0
        for i in range(n)[::-1]:
            if s[i] == '1':
                ans += j-i
                j -= 1
        return ans

print(Solution().minimumSteps("100"))