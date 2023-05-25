# 双指针
# 每次让短板变长，如此贪心
# 便能得到求得最优解

# 简单证明：
# 担心得无非是lr左右有更优解
# 但其实不会有的
# 已经被抛弃的lr左右肯定是已经被利用殆尽了的
# 能被抛弃说明另外一边有更高的，并将其利用殆尽
# 有更优解也已经被记录在ans中了

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            ans = max((r-l)*min(height[l], height[r]), ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
