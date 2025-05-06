'''
dp + 子序列

题目大意：找到一个最长子序列，使得其中 seq[i] != seq[i + 1] 冲突的次数小于等于k

思路：
相对比题目 3176，这道题扩大了 k的数据范围，所以之前 O(k*n^2)的算法肯定过不了，得想办法进行优化了
原本是枚举 i之前所有的 j，来进行状态转移
我们是否可以精确只从必要的地方进行转移而不全部进行枚举呢？
有的
当前是准备处理 dp[i][p]从何转移而来：
我们可以创建 mx[p][num]记录 p次冲突下以 num结尾的最大子序列长度（因为 num的取值范围大，所以进行哈希）
那么，当我们遍历到 nums[i]的时候，则可以直接 mx[p][nums[i]] + 1 （数字相同可以直接拼接）
但是还不够，如何处理从前面非 nums[i]的状态转移而来呢？
我们再建立一个 record，record[p][0/1]用于保存 p次冲突下的最大子序列长度以及结尾元素
如果 nums[i] != record[p][1]则有 dp[i][p] = max(dp[i][p], record[p-1][1] + 1)

这里可能有疑问，p次冲突下的最长子序列可能有多个，为什么我们只记录其中一个结尾元素就行呢？
分两种情况，如果记录的这个结尾元素不是 nums[i]，那么整合我们心意 record[p-1][1] + 1即可
如果结尾元素正好是 nums[i], 那其实 dp[i][p]在肯定通过前面的 mx正确更新了，我们跳过即可
以上两种都没问题，所以证毕！

另外，通篇看下来其实会发现 dp状态并不需要从之前的状态转移而来，所以其实可以把 dp压缩到一维列表
不过，当前状态就能过了，这里暂时先不做修改
'''

from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        dp = [[0]*(k+2) for _ in range(n+1)]  # dp[i][j] 表示以 nums[i]结尾的，有 j个冲突的最大长度
        ans = 1
        mx = [defaultdict(int) for _ in range(k+2)]  # mx[p][num]记录以 num结尾，p次冲突下的最大子序列长度
        record = [[0, 0] for _ in range(k+2)]  # record[p] 记录 p次冲突下的 (最长子序列结尾的元素，最长子序列的长度)
        for i in range(n):
            dp[i+1][0] = 1
            for p in range(k+1):
                dp[i+1][p] = mx[p][nums[i]] + 1
                if p > 0 and nums[i] != record[p-1][0]:
                    dp[i+1][p] = max(dp[i+1][p], record[p-1][1]+1)
                ans = max(ans, dp[i+1][p])

                # 维护 mx和 record
                mx[p][nums[i]] = max(mx[p][nums[i]], dp[i+1][p])  # 这里不能简单地在 nums[i]对应位+1，因为可能会从其他状态转移而来
                if dp[i+1][p] > record[p][1]:
                    record[p][1] = dp[i+1][p]
                    record[p][0] = nums[i]
        return ans


print(Solution().maximumLength(nums=[29, 30, 30], k=1))