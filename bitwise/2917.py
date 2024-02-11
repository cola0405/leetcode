from typing import List
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 1
        for i in range(31):
            cnt = 0
            for num in nums:
                if num&cur:
                    cnt += 1
            if cnt >= k:
                ans += cur
            cur <<= 1
        return ans