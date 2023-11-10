# 当 num 处于 (target, 2*target] 时，只需要 1 次
# 当 num = 2*target + 1时，需要 2 次 （可以是num//target，也可以是(num-1)//target）
# 当 num = 2*target - 1时，需要 1 次 （刚好是(num-1)//target）

# 从而得出结论，op的统计可以使用 (num-1)//target
# 最本质的原因在于 num%target 能整除时，其实只要分 1 次即可
# 然后恰好有 (num-1)//target 这个规律

from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(target):
            op = 0
            for num in nums:  # 直接均分,根据组数统计op
                op += (num-1)//target  # 优化
            return op <= maxOperations

        low = 1
        high = max(nums)
        while low < high:
            mid = (low+high)//2
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low

print(Solution().minimumSize([9], 2))
