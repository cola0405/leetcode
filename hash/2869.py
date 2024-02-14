from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        ans = 0
        while len(nums) > 0:
            num = nums.pop()
            if 1 <= num <= k:
                s.add(num)
            ans += 1
            if len(s) == k:
                return ans

