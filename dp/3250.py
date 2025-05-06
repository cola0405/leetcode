'''
多维 dp

题目大意：
给了一个列表 nums，然后允许我们自己构造两个数组 arr1和 arr2
数组中的项满足这个关系: arr1[i] + arr2[i] == nums[i]
问 arr1非递减，arr2非递增的不同方案有多少种

思路：
不难想到构建 dp[i][j]表示前 i个位，以数字 j结尾（这里的 j是对 arr1而言，arr2对应的数 = nums[i]-j）的合法方案数有多少种
因为 nums[i]的取值范围小，所以我们会想到拿 nums[i]结尾来作为一种状态
那状态之间如何进行转移呢？
dp[i][j]肯定会从 dp[i-1]中数字比 j小的那些状态进行转移（因为 arr1需要非递减）
所以枚举比 j小的数字 k（针对 arr1而言）
但是，同时我们还应该考虑到 arr2的非递增的合法性
上一个状态应该同时满足 arr1和 arr2的合法性，下面我们来分析：
如果 arr1当前选了数字 j（记为 a1），那么 arr2对应的数字就是 nums[i]-j（记为 a2）
我们前面说到我们会枚举上一个状态的数字 k（针对 arr1而言）
那么在上一个状态中，arr2对应的数字其实也是确定下来的 —— nums[i-1]-k
那么上一个状态只要满足条件 k <= a1 and nums[i-1]-k >= a2 即满足了两个数组的单调性，可以进行转移
'''


from typing import List
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 1000000007
        n = len(nums)
        mx = max(nums)
        dp = [[0]*(mx+1) for _ in range(n+1)]
        for i in range(mx+1):
            dp[1][i] = 1
        for i in range(1, n):
            for j in range(nums[i]+1):      # 第 i位，枚举arr1取哪个数字
                a1 = j
                a2 = nums[i]-j
                for k in range(j+1):          # 枚举 j之前的数字 k (Ps：k可以取到 j)
                    if k <= a1 and nums[i-1]-k >= a2:
                        dp[i+1][j] += dp[i][k]
                        dp[i+1][j] %= MOD
        return sum(dp[-1])%MOD

print(Solution().countOfPairs([2,3,2]))