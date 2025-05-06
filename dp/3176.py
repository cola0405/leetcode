'''
dp + 子序列

题目大意：找到一个最长子序列，使得其中 seq[i] != seq[i + 1] 冲突的次数小于等于k

思路：
第一时间可能想 dp[i][j]表示前 i个数字，有 j个冲突的最大长度
但是缺少以谁结尾的信息，进而想到 dp[i][j][p]表示到第 i位，以 nums[j]结尾的，有 p个冲突的最大长度
时间复杂度 O(k*n^2) 按道理来说不会超时的，但是就是过不了。。。
所以考虑优化方案
这里其实可以把 dp数组优化到 2维
dp[i][p] 表示以 nums[i]结尾的，有 p个冲突的最大长度
在申请空间上省了一些时间就可以过了
然后说下，这个状态下如何转移

枚举 i前面的各个数字 j，如果 nums[i] == nums[j]则 dp[i][p] = dp[j][p]+1 (p是冲突次数，也需要去枚举的，所以下面是三层循环)
如果是 nums[i] != nums[j] 则 dp[i][p] = dp[j][p-1] + 1

需要注意的是，k有可能等于 0，但我们也需要到最里面那层循环去更新 dp
所以需要会有(k+1)的特殊处理
[p+1] 则是因为涉及到了 [p-1]
'''
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0]*(k+2) for _ in range(n)]
        ans = 1
        # dp初始化
        dp[0][1] = 1
        for i in range(1, n):
            for j in range(i):      # 枚举之前出现过的数字(同个数字可能出现多次，这些数字的状态不能堆叠)
                for p in range(k+1):
                    if nums[i] == nums[j]:
                        dp[i][p+1] = max(dp[i][p+1], dp[j][p+1] + 1)
                    else:
                        dp[i][p+1] = max(dp[i][p+1], dp[j][p] + 1)
                    ans = max(ans, dp[i][p+1])
        return ans