# 贪心解决另辟蹊径解决选/不选问题

# 为什么可以取到mid之后的为low呢？
# ①low的更新不会影响mid，low是往小了取 （mid的更新同样也不影响low，只有大于low的才能给mid取到）
# ②尽量压低low和mid，这样才能尽可能取到递增的第三位 -- 这是为什么要更新的原因，也是该贪心的核心思想

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        low = float('inf')  # 初始值设置为inf很重要
        mid = float('inf')

        for num in nums:
            if num <= low:    # 有更小的就取更小的
                low = num
            elif num <= mid:  # 到这说明num已经大于low
                mid = num
            elif num>mid:     # num>mid说明mid已经不再是inf,也说明low已有人选
                return True   # 到这说明3个数已成型
        return False