from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    ans = max(ans, nums[i]^nums[j])
        return ans