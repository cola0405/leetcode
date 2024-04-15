from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        cnt = sorted(cnt.items(), key=lambda x: (x[1], -x[0]))
        ans = []
        for num, freq in cnt:
            ans += [num]*freq
        return ans