'''
纯暴力的话时间复杂度O(n^3)
dp优化到O(n^2)

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        min_inx = 0
        max_inx = 0
        dp = [[False]*(n+1) for _ in range(n+1)]
        for i in range(n)[::-1]:
            dp[i][i] = True            # 单个字符就是一个回文串
            for j in range(i+1, n):
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    if j-i > max_inx-min_inx:       # 保存最长回文串的索引
                        min_inx = i
                        max_inx = j
        return s[min_inx:max_inx+1]

print(Solution().longestPalindrome("babad"))