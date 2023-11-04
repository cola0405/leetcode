# dp[i] 和 dp[i-1] 的转移与s[i-1] s[i]有关，那就开二维数组来dp
# dp[i][0] 表示[0,i]递增序列以0结尾时所需的操作次数
# dp[i][1] 表示[0,i]递增序列以1结尾时所需的操作次数

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0,0] for _ in range(n)]
        if s[0] == '0':
            dp[0][1] = 1
        else:
            dp[0][0] = 1

        for i in range(1, n):
            if s[i] == '0':
                dp[i][0] = dp[i-1][0]
                # 如果要改以1结尾，需要操作数+1，然后前一位为0和1都可以
                dp[i][1] = min(dp[i-1][1], dp[i-1][0])+1
            elif s[i] == '1':
                # 如果要改以0结尾，需要操作数+1，然后前一位只能是0
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])  # 以1结尾，不需要额外改
        return min(dp[n-1][0], dp[n-1][1])

print(Solution().minFlipsMonoIncr("010110"))