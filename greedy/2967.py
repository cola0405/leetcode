# 中位数贪心

from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def cost(y):
            res = 0
            for num in nums:
                res += abs(num-y)
            return res

        nums.sort()
        mid = 0
        if len(nums)%2 != 0:
            mid = nums[len(nums)//2]
        else:
            mid = (nums[len(nums)//2] + nums[len(nums)//2-1]) // 2

        right = mid
        while str(right) != str(right)[::-1]:
            right += 1

        left = mid
        while str(left) != str(left)[::-1]:
            left -= 1

        return min(cost(left), cost(right))
