from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -float('inf')
        s = sum(nums[:k])
        for i in range(len(nums)-k):
            max_sum = max(s, max_sum)
            s = s-nums[i]+nums[i+k]
        max_sum = max(s, max_sum)
        return max_sum/k

print(Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
