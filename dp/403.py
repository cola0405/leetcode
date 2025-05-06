'''
多维 dp

题目大意：给了一些石头的位置，每次青蛙只能往前跳
如果某次跳跃了距离 x，那么下一次跳跃青蛙可以选择跳跃距离 x-1, x, x
确认是否青蛙能跳到最后一个石头上

思路：
不难想到这里肯定是要设计 2维的 dp
除了 [i]另外一个参数设置为什么好呢？
关注到题目里有一个信息很关键，就是青蛙上一次跳了多远
那么我们有 dp[i][j]表示青蛙跳到第 i个石头上，且上一次跳跃的距离为 j的可行性，1表示可以到
然后考虑这么设置是否会超时，看到虽然 stone[i]的取值范围虽然很大，但是 n小，然后每次距离最多 +1，所以 dp里层我们最多才开到 2000，所以没关系
然后我们来考虑状态如何转移
肯定是要往前找可以转移的状态 O(n^2)的算法在这里也不超时
首先求出 d = stone[i] - stone[j]
然后我们去看 j位置有没有可能通过跳跃距离 x-1, x, x+1 跳跃到 stone[i]

'''


from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[1][0] = 1        # 初始状态
        for i in range(n):
            for j in range(i):
                # 看 j位置有没有可能通过跳跃距离 x-1, x, x+1 跳跃到 stone[i]
                d = stones[i] - stones[j]
                if d <= n: dp[i+1][d] |= dp[j+1][d]
                if d <= n: dp[i+1][d] |= dp[j+1][d-1]
                if d+1 <= n: dp[i+1][d] |= dp[j+1][d+1]
        return sum(dp[n]) > 0

print(Solution().canCross( [0,1,3,5,6,8,12,17]))