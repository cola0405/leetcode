from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()
        n = len(nums)
        for i in range(n):
            idx[nums[i]] = i

        for i in range(n):
            num = target-nums[i]
            if num in idx:  # 双if
                if idx[num] != i:
                    return [i, idx[num]]
                idx.pop(nums[i])

print(Solution().twoSum(nums = [3,3], target = 6))


