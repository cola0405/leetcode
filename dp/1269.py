'''
多维dp

题目大意：从位置 0出发，给了可移动的次数以及移动范围，问最后仍然在位置 0的方案数有多少

思路：
不难想到构造 dp[i][j]表示第 i次移动处于位置 j的方案数
状态怎么转移呢？
位置 j可以从上一个状态 dp[i-1]的 j+1, j-1 或者 j来（停留在原地）
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
然后转移的时候时候注意一下边界问题即可

但是，常规的 dp会有超时、超内存的问题（500*10^6的 dp数组）
优化可以从几方面入手
1.虽然 arrLen的长度可以到 10^6,但是步数总共才 500，每次走一步，根本到不了那么远，所以数组不用开到 10^6那么大
2.因为我们要求的是最终停留在位置 0的方案数，所以我们只考虑 step//2的范围即可

'''


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1000000007
        right = min(steps//2, arrLen-1)
        dp = [[0]*(right+1) for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(steps):
            for j in range(right+1):
                dp[i+1][j] += dp[i][j]
                if j+1 < len(dp[0]):
                    dp[i+1][j] += dp[i][j+1]
                if j-1 >= 0:
                    dp[i+1][j] += dp[i][j-1]
                dp[i+1][j] %= MOD
        return dp[steps][0]

print(Solution().numWays(steps = 3, arrLen = 2))