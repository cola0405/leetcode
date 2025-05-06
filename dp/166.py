'''
dp

题目大意：股票可以多次买卖，求最大收益

思路：
设置状态 dp[i] 表示到第 i天能获取的最大收益
如何进行状态转移呢？
我们先尝试思考 dp[i-1] 和 dp[i]的关系
关键点就在于我是否要在第 i天的股票价格时卖出
联想到前面我要在哪一天买入呢？
结论：我们只考虑 i-1 那天就行了
我们假设在更前面有一天 j的股价更低，看似我们需要从 dp[j] 转移过来
但是，我们完全可以在第 j天买入，然后在第 i-1天卖出赚取其中的利润
然后如果第 i天的股价比 i-1的股价更高
我们就在第 i-1天再继续买入，然后到第 i天卖出

综上，我们进行状态转移时，只考虑 dp[i-1]即可
（以上推理过程有一个大前提，不限制交易次数，我们才可以直接从dp[i-1]转移，而题目 123 则有进行交易次数的限制）

'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        for i in range(n-1):    # 下面有 prices[i+1] 所以进行 n-1
            # -prices[i] 表示在那天的股票价格买入，所以相当于那一天的最大收益要减去一部分
            dp[i+1] = max(dp[i], dp[i] - prices[i] + prices[i+1])       # i+1是做偏移
        return dp[-1]

print(Solution().maxProfit([7,1,5,3,6,4]))