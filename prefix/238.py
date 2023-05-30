from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        for i in range(1, len(l)):
            l[i] = l[i-1]*nums[i-1]
        r = [1]*len(nums)
        for i in range(len(r)-1)[::-1]:
            r[i] = r[i+1]*nums[i+1]

        ans = [0]*len(nums)
        for i in range(len(ans)):
            ans[i] = l[i]*r[i]
        return ans

print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))