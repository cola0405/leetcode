# prefix + hash
# use prefix to record the amount of '01' between interval
# if there do have a pair of (i,j) with the same prefix
# which means that '01' of interval is balanced, the amount of '0' and '1' is the same
# we use the hash table to record the left-most index of pre

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        inx = dict()
        inx[0] = -1
        ans = 0
        pre = 0
        d = {0:-1, 1:1}
        for i in range(len(nums)):
            pre += d[nums[i]]

            if pre not in inx:  # for saving the left-most index
                inx[pre] = i
            else:
                ans = max(ans, i-inx[pre])  # the same endpoints
        return ans

print(Solution().findMaxLength([0,1]))