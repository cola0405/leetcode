# difference + greedy

from typing import List
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        diff = [nums[0]]
        for i in range(1,len(nums)):        # build difference first
            diff.append(nums[i]-nums[i-1])

        for i in range(len(nums)):          # try to fix the array in greedy way
            if diff[i] > 0:
                if i+k < len(nums):         # with fixed length -- k
                    diff[i+k] += diff[i]
                elif i+k > len(nums):   
                    return False
            elif diff[i] < 0:               # we can only do the decreasement
                return False
        return True

print(Solution().checkArray(nums = [2,2,3,1,1,0], k = 3))
