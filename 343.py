class Solution:
    def integerBreak(self, n: int) -> int:
        # 抽象一下，这其实是一个背包问题


        dp = [0]*(n+1)  # dp[i]表示和为i的整数们的最大乘积
        dp[1] = 1
        # 方程dp[i-num]*num
        # 无限背包问题,所以dp遍历作外层
        for i in range(1,n+1):
            for num in range(1,i):
                # 嵌套的max用于处理那个数拆与不拆
                # 因为有时拆成多个数的积反而得到的值更小，比如说:3
                dp[i] = max(max(dp[i-num], i-num)*num, dp[i])

        return dp[-1]

Solution().integerBreak(10)
