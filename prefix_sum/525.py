# longest interval with the same endpoints in diff

# see also find-longest-subarray-lcci.py
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = [0]
        for num in nums:
            if num == 1:
                diff.append(diff[-1]+1)
            else:
                diff.append(diff[-1]-1)

        inx = dict()
        for i in range(len(diff))[::-1]:
            if diff[i] not in inx:
                inx[diff[i]] = i
        ans = 0
        for i in range(len(diff)):
            ans = max(ans, inx[diff[i]]-i)
        return ans
