# double monotonic stack
# pop while x > s[-1] -- increasing stack —— top is the smallest
# pop while x < t[-1] -- decreasing stack —— top is the largest

# push the numbers in increasing stack-s first
# the elements pop out from s should be in t (decreasing stack)
# for the elements in t(decreasing stack) -- there must exist elements greater than it
# so when the new element x is greater than the t[-1] -- x is the next greater element
from typing import List
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        s = []
        t = []

        for i in range(n):
            while t and nums[i] > nums[t[-1]]:
                ans[t.pop()] = nums[i]
            tmp = []
            while s and nums[i] > nums[s[-1]]:
                tmp.append(s.pop())   # the numbers from s must be greater than t[-1]
            t += tmp[::-1]
            s.append(i)
        return ans

print(Solution().secondGreaterElement([2,4,0,9,6]))