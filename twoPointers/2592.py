from typing import List
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums)-1
        ans = 0
        for i in range(len(nums)-1)[::-1]:
            if nums[j] > nums[i]:
                ans += 1
                j -= 1
        return ans

print(Solution().maximizeGreatness([1,3,5,2,1,3,1]))