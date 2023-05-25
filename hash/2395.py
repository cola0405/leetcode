from typing import List
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        record = set()
        for i in range(len(nums)-1):
            s = nums[i]+nums[i+1]
            if s in record:
                return True
            else:
                record.add(s)
        return False

print(Solution().findSubarrays(nums = [1,2,3,4,5]))
