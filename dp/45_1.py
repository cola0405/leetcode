# 留意题目提供的条件：
# ① 可以跳到可达范围内容易位置
# ② 必定能够到达终点

# 看到条件②的时候，其实很容易想到从后往前推
# 会发现有若干个位置可以到endpoint，在这些点中，最左边的点是最优解
# 因为如果可通过其他点到endpoint，那也一定可以通过最左边的点到endpoint
# 然后就是用贪心的方法求上上个节点

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        i = len(nums)-1
        while i != 0:  # 不知道几次就while true
            for j in range(i):
                if i-j <= nums[j]:
                    i = j
                    ans += 1
                    break
        return ans


print(Solution().jump([2,3,0,1,4]))