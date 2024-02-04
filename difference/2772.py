# difference + greedy
from typing import List
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        diff = [nums[0]]
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])

        for i in range(len(nums)):
            if diff[i] > 0:
                if i+k < len(nums):
                    diff[i+k] += diff[i]
                elif i+k > len(nums):   # can't decrease with fixed k size subarray
                    return False
            elif diff[i] < 0:   # no way to save negative number
                return False
        return True

print(Solution().checkArray(nums = [2,2,3,1,1,0], k = 3))
