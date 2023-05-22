from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)    # 不同正整数的数量就是要操作的次数
        if 0 in nums:
            return len(nums)-1
        return len(nums)

print(Solution().minimumOperations(nums = [1,5,0,3,5]))