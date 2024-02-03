# prefix + xor + interval-hash
# we need to count the number of interval that the xor result is 0

from typing import List
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        ans = 0
        for num in nums:
            pre ^= num
            ans += cnt[pre]     # pre[j] == pre[i] means the xor of all elements between interval is 0
            cnt[pre] += 1
        return ans