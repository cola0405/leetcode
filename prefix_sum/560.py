# the effect of the interval is k
# if there do hava (pre-k) exist, which means there do exist the interval with sum k

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        ans = 0
        pre = 0
        for num in nums:
            cnt[pre] += 1   # cnt[0] += 1
            pre += num
            ans += cnt[pre-k]   # (pre-k) + k = pre means there do exist the interval with sum k
        return ans

print(Solution().subarraySum([1,1,1],2))
