class Solution:
    def numSquares(self, n: int) -> int:
        import math
        # build table
        nums = [i**2 for i in range(int(math.sqrt(n))+1)]

        dp = [float('inf')]*(n+1)  # dp[i]表示得到i需要的最少完全平方数
        dp[0] = 0
        for i in range(1,n+1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i-num]+1, dp[i])
        print(dp[-1])

Solution().numSquares(12)

