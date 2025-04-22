'''
dp 记录状态

人其实就分为两种状态：
1. 知道秘密，但是还没办法传播
2. 知道秘密，也可以进行传播

在这里，可以传播秘密的人是关键，但是这个量会增加、也会减少（忘记秘密）
如何正确维护呢？
因为与之前的状态有关 —— 什么时候知道的秘密 
不难想到 dp[i-delay] dp[i-forget] 可以分别维护人数增加的量和减少的量
所以我们可以把 dp[i] 定义为第 i 天新增的人数

然后用额外的变量 active 表示当前能够传播秘密的人数
然后在第n天知道秘密的人数，就是 dp[n]往前倒 forget天的人数之和
'''


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0]*(n+1)      # dp[i] 表示第 i 天新增的人数
        dp[1] = 1
        active = 0             # 当前能够传播秘密的人数
        for i in range(2,n+1):
            if i-delay >= 1:
                active = (active + dp[i-delay]) % mod         # 利用dp去维护第i天能够传播秘密的人数
            if i-forget >= 1:
                active = (active - dp[i-forget] + mod) % mod
            dp[i] = active
        return sum(dp[n+1-forget: n+1]) % mod

print(Solution().peopleAwareOfSecret(6,2,4))