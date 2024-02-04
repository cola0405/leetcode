# 线性问题，二分求解

# 然后check()有优化
# 详见1760_1.py

from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(target):
            op = 0
            for num in nums:  # 直接均分,根据组数统计op
                if num%target == 0:
                    op += num//target - 1
                else:
                    op += num//target
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
