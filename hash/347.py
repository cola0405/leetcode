from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort(key=lambda num: count[num], reverse=True)
        return nums[:k]

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
