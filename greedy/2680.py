# greedy + prefix + suffix

# in greedy strategy, to make the result as large as possible
# we need to apply all k left shift operation to only one nums[i]
# but how to choose the nums[i] -- we can calculate all the results and pickup the maximum
# 10^5 -- we have to optimize the calculation

# use prefix + suffix -- (pre | nums[i]<<k | suffix[i+1])
from typing import List
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        suffix = [0]*(len(nums)+1)
        for i in range(len(nums))[::-1]:
            suffix[i] = nums[i] | suffix[i+1]

        ans = 0
        pre = 0
        for i in range(len(nums)):
            ans = max(ans, pre | nums[i]<<k | suffix[i+1])  # try the unique<<k
            pre |= nums[i]
        return ans

print(Solution().maximumOr(nums = [87,97,17,20,5,11], k = 9))



