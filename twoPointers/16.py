# sort + O(n) + two pointers make O(n)  -- O(n^2)
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s-target) < abs(ans-target):
                    ans = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return ans

print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))

