from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_sorted():
            for inx in range(len(cur)-1):
                if cur[inx] >= cur[inx+1]:
                    return False
            return True

        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                cur = nums[:i] + nums[j+1:]
                if is_sorted():
                    ans += 1
        return ans

print(Solution().incremovableSubarrayCount([8,7,6,6]))