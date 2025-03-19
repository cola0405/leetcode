# dp[i] 会等于 i往前 zero或 one 位的 dp之和（因为只有两种方式）

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0]*high
        for i in range(high+1):
            if i >= zero: dp[i] = dp[i-zero]
            if i >= one: dp[i] = (dp[i] + dp[i-one]) % (10**9+7)
        return sum(dp[low:high+1])%(10**9+7)