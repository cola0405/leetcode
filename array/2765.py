from typing import List
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = 1
        for i in range(len(nums)):
            flag = 1
            cnt = 1
            while i<len(nums)-1 and nums[i]+flag==nums[i+1]:
                flag *= -1
                cnt += 1
                i += 1
            ans = max(ans, cnt)
        if ans == 1:
            return -1
        return ans

print(Solution().alternatingSubarray([2,3,4,3,4]))

