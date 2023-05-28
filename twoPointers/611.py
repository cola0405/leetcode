from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            k = 0
            for j in range(i)[::-1]:
                while k<j and nums[k]+nums[j] <= nums[i]:
                    k += 1
                if j<=k:
                    break
                ans += j-k
        return ans

print(Solution().triangleNumber(nums = [2,2,3,4]))
