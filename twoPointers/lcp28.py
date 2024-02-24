from typing import List
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        MOD = int(1e9+7)
        nums.sort()
        i = 0
        j = len(nums)-1
        ans = 0
        while i < j:
            while i < j and nums[i] + nums[j] > target:
                j -= 1
            ans = (ans + j-i) % MOD
            i += 1
        return ans