# pattern + 2^n recursion + congruence + sort

from typing import List
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = (10**9+7)
        nums.sort()
        ans = 0
        s = 0
        for i in range(len(nums)):
            ans = (ans + nums[i]**2 * (s+nums[i])) % MOD
            s = (s*2 + nums[i]) % MOD   # added after -- deduce to figure out
        return ans


print(Solution().sumOfPower([2,1,4]))