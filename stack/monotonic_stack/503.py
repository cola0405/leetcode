from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        s = []
        nums += nums
        for i in range(2*n):
            while s and nums[i] > nums[s[-1]]:
                inx = s.pop()
                if inx < n:
                    ans[inx] = nums[i]
            s.append(i)
        return ans

print(Solution().nextGreaterElements([1,2,1]))