from typing import List
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            tmp = i
            bit_cnt = 0
            while i > 0:
                if i&1:
                    bit_cnt += 1
                i >>= 1
            if bit_cnt == k:
                ans += nums[tmp]
        return ans