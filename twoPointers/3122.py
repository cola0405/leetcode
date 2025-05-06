'''
dp + 矩阵

题目大意：给定一个二维列表，我们要确保一列中所有数字都相等，同时确保相邻两列的数字不同
求最小的操作次数

思路：
并不是所有的二维矩阵 dp都要用针对二维矩阵中的每一位 [i][j]来进行转移
在这道题里，我们针对每一列进行 dp会更合适
dp[j][k] 表示把前 j列处理完成，并且第 j列是数字 k的最小操作次数
那么，我们只需要枚举上一个状态的所有数字，然后进行状态转移即可

要注意的是，为了方便 dp，我们需要预处理一个数组，cost[j][k]表示把第 j列变为 数字 k所需要的代价
另外因为涉及到[j-1] 所以我们需要对 dp[0]那一列进行初始化
'''

from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')]*10 for _ in range(m+1)]        # 初始值要设置为 inf
        for k in range(10): dp[0][k] = 0        # dp数组初始化
        cost = [[0]*10 for _ in range(m)]       # 预处理 cost[j][k] 把第 j列变为 数字 k所需要的代价
        for j in range(m):
            cnt = defaultdict(int)
            for i in range(n): cnt[grid[i][j]] += 1
            for k in range(10): cost[j][k] = n - cnt[k]

        # 状态转移
        for j in range(m):
            for k in range(10):         # 枚举当前第 j列可能的数字
                for p in range(10):     # 枚举上一个状态的数字
                    if k == p: continue     # 跳过相邻 2列相同的数字的情况
                    dp[j+1][k] = min(dp[j+1][k], dp[j][p] + cost[j][k])
        return min(dp[m])



print(Solution().minimumOperations(grid = [[1,1,1],[0,0,0]]))
