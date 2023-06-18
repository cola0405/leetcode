from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        res = [0]*len(nums)
        for k in range(len(nums)):
            if nums[k]%2 == 0:
                res[i] = nums[k]
                i += 2
            else:
                res[j] = nums[k]
                j += 2
        return res

print(Solution().sortArrayByParityII([4,2,5,7]))