from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        for i in range(len(nums)):
            if nums[i] in idx and i-idx[nums[i]]<=k:
                return True
            idx[nums[i]] = i
        return False

print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))