from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        from collections import Counter
        cnt = Counter(nums)
        n = max(nums)
        for num in range(1,n-1):
            if cnt[num] != 1:
                return False

        return cnt[n] == 2