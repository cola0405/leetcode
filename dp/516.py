'''
区间 dp + 倒序 dp

dp[i][j] 表示 s[i,j] 最长回文子序列的长度
注意，子序列其实是把问题简单化了！因为我们不关心相邻的字符


'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n)[::-1]:            # 因为状态转移涉及到 i+1，所以需要倒序 dp
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])      # 虽然s[i:j+1] 不是回文，但是 s[i+1:j] 或 s[i:j] 可能是回文
        return dp[0][-1]

print(Solution().longestPalindromeSubseq("bbbab"))
