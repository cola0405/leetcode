# prefix sum + congruence + modulo-hash(count the result of mod)

# the cnt is actually the interesting number in the interval
# we can use prefix sum to get the cnt by pre[j] - pre[i-1]

# then we need to figure out how many pairs could be interesting
# and fit the equation (pre[j] - pre[i-1]) % module == k
# transform the equation -- pre[j]%module - k == pre[i-1]%module
# the problem is transformed -- how many pre[i-1]%module exist
# we can use the hash-table to count it

# what's more, (pre[j]%module - k) may be negative
# a solution to this problem is -- add modulo and mod it

from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] += 1
        pre = 0
        ans = 0

        for num in nums:
            pre += num%modulo == k
            ans += cnt[(pre%modulo - k + modulo)%modulo]    # prevent (pre%modulo - k) become negative
            cnt[pre%modulo] += 1
        return ans

print(Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0))