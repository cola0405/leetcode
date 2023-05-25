# 定k，然后i、j双指针
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def idx_no_repeat(val):
            if val not in d:
                return False

            for idx in d[val]:
                if idx != i and idx != j:
                    return True
            return False  # can't find available val


        d = {num:[] for num in nums}
        for i in range(len(nums)):
            d[nums[i]].append(i)

        ans = []
        record = set()
        from itertools import permutations
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                target = [nums[i],nums[j],-s]
                # avoid the repeat index
                if idx_no_repeat(-s) and tuple(target) not in record:
                    ans.append(target)
                    # avoid repeat elements
                    for item in permutations((nums[i], nums[j], -s)):
                        record.add(item)

        return ans