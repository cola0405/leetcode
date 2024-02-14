# 2760_1.py is better
from typing import List
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            if nums[l]%2 != 0:
                continue
            for r in range(l, n):
                # check
                flag = 1
                for i in range(l,r):
                    if nums[i]%2 == nums[i+1]%2:
                        flag = 0
                        break
                for i in range(l,r+1):
                    if nums[i] > threshold:
                        flag = 0
                        break
                if flag:
                    ans = max(ans, r-l+1)
        return ans