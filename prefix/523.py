# prefix + congruence-hash count
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        for i in range(len(nums)):
            num = nums[i]
            last = pre
            pre += num
            # make sure the length of the interval is greater than 2
            if (pre%k != last%k or cnt[pre%k]>1) and cnt[pre%k] > 0:
                return True
            cnt[pre%k] += 1
        return False
