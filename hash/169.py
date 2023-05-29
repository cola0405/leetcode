from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        target = len(nums)/2
        for num in count:
            if count[num]>target:
                return num