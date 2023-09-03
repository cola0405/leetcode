# 二维dp

# 一维很明显已经处理不了了
# 区间问题 -- i到j
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        max_l = 0
        max_r = 0
        dp = [[0]*n for _ in range(n)]
        for r in range(1, n):
            for l in range(r)[::-1]:
                if s[l] == s[r] and (r-l<=2 or dp[l+1][r-1]):
                    dp[l][r] = 1
                    if r-l+1 > max_r-max_l+1:
                        max_l = l
                        max_r = r
        return s[max_l: max_r+1]

print(Solution().longestPalindrome("cbbd"))
