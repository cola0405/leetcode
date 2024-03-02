from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n//2
        ans = 0
        for num in nums:
            ans += abs(num-nums[mid])
        return ans

print(Solution().minMoves2([1,2,3]))