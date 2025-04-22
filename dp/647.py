'''

区间 dp
dp[i][j] 表示[i,j]范围内回文子串的数量
那就双重循环枚举所有子串 + dp优化解决问题 —— 时间复杂度O(n^2)

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = n
        for i in range(n)[::-1]:        # 逆序 dp 是因为状态转移依赖于dp[i+1][]
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = 1
                    ans += 1
        return ans

print(Solution().countSubstrings("aaa"))