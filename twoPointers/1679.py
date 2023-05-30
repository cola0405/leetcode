from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j] == k:
                ans += 1
                i += 1
                j -= 1
            elif nums[i]+nums[j] > k:
                j -= 1
            else:
                i += 1
        return ans

print(Solution().maxOperations(nums = [3,1,3,4,3], k = 6))