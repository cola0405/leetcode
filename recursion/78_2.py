# bits 解决拿/不拿问题

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        for digits in range(2**n):
            tmp = []
            for i in range(n):
                if digits & 1:
                    tmp.append(nums[n-1-i])
                digits >>= 1
            ans.append(tmp)
        return ans

print(Solution().subsets([1,2,3]))