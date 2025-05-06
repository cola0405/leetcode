'''
状态机dp

题目大意：有两种饮料，不同时间其提供的能量不同
可以持续喝某一种饮料，能量值会叠加
如果选择切换饮料，则需要等待一小时之后才能继续喝，然后求能量最大值

思路：与股票的冷冻期类似，那就不从 i-1转移，从 i-2转移即可
然后 i-2的话，要处理好越界问题
dp[i][0/1] 表示到第 i小时喝 A/B饮料能获取的能量最大值
'''

from typing import List
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0,0] for _ in range(n+1)]
        for i in range(n):
            dp[i+1][0] = dp[i][0]+energyDrinkA[i]
            dp[i+1][1] = dp[i][1]+energyDrinkB[i]

            if i-1 >= 0:
                dp[i+1][0] = max(dp[i+1][0], dp[i-1][1]+energyDrinkA[i])    # 切换饮料，b到 a
                dp[i+1][1] = max(dp[i+1][1], dp[i-1][0]+energyDrinkB[i])    # 切换饮料，a到 b
        return max(dp[-1])

print(Solution().maxEnergyBoost([4,1,1], [1,1,3]))