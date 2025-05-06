'''
dp(涉及到模状态的 dp)

题目大意：数组内任意选元素，使得总和是 3的倍数，然后让总和尽可能大

思路：
这个是数字选与不选的问题，状态dp[i] 明显不够，因为不知道之前模的状态
所以把状态设置为 dp[i][j] 表示前 i个数字和 mod3 = j的最大和
那状态之间怎么转移呢？
对于第 i个数，如果不选，则直接为 dp[i-1][j]
选了之后，其总和的余数为 (j+nums[i])%3 会转移到这里
所以，这里的 dp写法会比较有意思，考虑的不是谁转移到 dp[i][j]而是 dp[i][j]会转移到哪里
dp[i][(j+nums[i])%3] = max(dp[i-1][(j+nums[i])%3], dp[i][j] + nums[i])

这里还要注意的是 dp初始状态的设置，具体看下面的解释
'''

from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*3 for _ in range(n+1)]
        # 这两个初始状态不能设置为 0，因为初始状态下，余数为 1和 2的状态根本不存在，不可以设置为 0
        dp[0][1] = dp[0][2] = float('-inf')
        for i in range(n):
            for j in range(3):
                dp[i+1][(j+nums[i])%3] = max(dp[i][(j+nums[i])%3], dp[i][j]+nums[i])
        return dp[-1][0]
print(Solution().maxSumDivThree([3,6,5,1,8]))