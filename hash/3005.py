from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        return list(cnt.values()).count(max_cnt) * max_cnt
