# prefix + hash count + congruence

# do not still consider of how many pairs (i,j)
# use congruence to optimize the problem
# determine how many (pre[j] - pre[i-1]) % k == 0
# is actually calculate how many pre[j]%k == pre[i-1]%k
# we can use hash table to store the number of pre[j]%k before

# as long as the pre%k is the same
# the equation (pre[j] - pre[i-1]) % k == 0 will also be true -- by congruence
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        pre = 0
        for num in nums:
            pre += num
            ans += cnt[pre%k]
            cnt[pre%k] += 1
        return ans

print(Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))