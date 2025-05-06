'''
多维dp

题目大意：求满足要求的最长子序列长度

思路：
不难想到 dp[i][j]表示前 i个字符，以字母 j结尾的最长满足要求的子序列长度
每次枚举上一个状态 dp[i-1][j]的所有字母到当前字符 s[i]即可
然后因为这里字母总共就 26种，所以双重循环处理 n=10^5是没问题的
'''


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0]*26 for _ in range(n+1)]
        for i in range(n):
            x = ord(s[i])-ord('a')      # 转化第 i个字符对应的 index
            for j in range(26):                             # 枚举 26个字母到第 i个字符的状态
                dp[i+1][j] = max(dp[i][j], dp[i+1][j])      # 不选第 i个字符，各个位都要继承上一个状态
                if abs(j - x) <= k:                         # 如果相邻字符满足了要求，则尝试选取
                    dp[i+1][x] = max(dp[i+1][x], dp[i][j]+1)
        return max(dp[n])

print(Solution().longestIdealString(s = "acfgbd", k = 2))