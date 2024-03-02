# sort + O(n) + two pointers make O(n)  -- O(n^2)
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        ans = float('inf')
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s-target) < min_diff:
                    min_diff = abs(s-target)
                    ans = s

                while k-1 > j and s > target:
                    k -= 1
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < min_diff:
                        min_diff = abs(s - target)
                        ans = s
                j += 1
        return ans

print(Solution().threeSumClosest(nums = [-2,-1,1,4], target = 0))

