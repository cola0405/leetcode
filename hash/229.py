from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        threshold = len(nums)/3
        return [num for num in count if count[num]>threshold]