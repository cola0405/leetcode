# dual-monotonic stack
# base on problem 84

from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1]*n  # default -1 means all elements from cur to left-end can contribute for rectangle
        ms = []
        for i in range(n):
            while ms and nums[i] <= nums[ms[-1]]:
                ms.pop()
            if ms:
                left[i] = ms[-1]
            ms.append(i)

        right = [n]*n  # default n means all elements from cur to right-end can contribute for rectangle
        ms = []
        for i in range(n)[::-1]:
            while ms and nums[i] <= nums[ms[-1]]:
                ms.pop()
            if ms:
                right[i] = ms[-1]
            ms.append(i)

        ans = 0
        for i in range(n):
            if left[i] < k < right[i]:
                ans = max(ans, nums[i]*(right[i]-left[i]-1))
        return ans